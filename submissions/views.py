from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from problems.models import CodingProblem
from .models import Submission

from users.models import UserStreak

from datetime import date, timedelta

import io
import sys
import builtins


def run_code(request):

    if request.method == "POST":

        code = request.POST.get("code", "")
        custom_input = request.POST.get(
            "custom_input",
            ""
        )

        old_stdout = sys.stdout
        old_input = builtins.input

        redirected_output = io.StringIO()

        inputs = custom_input.splitlines()

        input_index = 0

        def mock_input(prompt=""):

            nonlocal input_index

            if input_index < len(inputs):

                value = inputs[input_index]
                input_index += 1

                return value

            return ""

        sys.stdout = redirected_output
        builtins.input = mock_input

        try:

            exec(code)

            output = redirected_output.getvalue()

        except Exception as e:

            output = str(e)

        finally:

            sys.stdout = old_stdout
            builtins.input = old_input

        return JsonResponse({
            "output": output
        })

    return JsonResponse({
        "output": "Invalid Request"
    })


def judge_python_code(code, test_cases):

    passed = 0
    total = 0

    if not test_cases:

        return {
            "status": "No Test Cases",
            "score": 0,
            "runtime": "0 sec",
            "memory": "0 MB"
        }

    for line in test_cases.strip().split("\n"):

        if "|" not in line:
            continue

        test_input, expected_output = line.split("|")

        total += 1

        old_stdout = sys.stdout
        old_input = builtins.input

        redirected_output = io.StringIO()

        inputs = test_input.split(",")

        input_index = 0

        def mock_input(prompt=""):

            nonlocal input_index

            if input_index < len(inputs):

                value = inputs[input_index]
                input_index += 1

                return value.strip()

            return ""

        sys.stdout = redirected_output
        builtins.input = mock_input

        try:

            exec(code)

            output = redirected_output.getvalue().strip()

            if output == expected_output.strip():

                passed += 1

        except Exception:
            pass

        finally:

            sys.stdout = old_stdout
            builtins.input = old_input

    score = int(
        (passed / total) * 100
    ) if total else 0

    if passed == total:

        status = "Accepted"

    elif passed > 0:

        status = "Partially Accepted"

    else:

        status = "Wrong Answer"

    return {

        "status": status,
        "score": score,
        "runtime": "0.01 sec",
        "memory": "14 MB"

    }


def generate_ai_review(code):

    review = []

    if "for" in code:

        review.append(
            "Good use of loops."
        )

    if "dict" in code or "{}" in code:

        review.append(
            "Efficient dictionary usage."
        )

    if len(code.splitlines()) < 10:

        review.append(
            "Concise solution."
        )

    review.append(
        "Consider adding comments for readability."
    )

    return review


def submit_solution(request, problem_id):

    problem = get_object_or_404(
        CodingProblem,
        id=problem_id
    )

    if request.method == "POST":

        code = request.POST.get("code")

        language = request.POST.get(
            "language",
            "python"
        )

        result = judge_python_code(
            code,
            problem.test_cases
        )

        ai_review = generate_ai_review(
            code
        )

        Submission.objects.create(

            user=request.user,
            problem=problem,
            code=code,
            language=language,
            status=result["status"],
            score=result["score"],
            runtime=result["runtime"],
            memory=result["memory"]

        )

        today = date.today()

        streak, created = UserStreak.objects.get_or_create(
            user=request.user
        )

        if streak.last_submission_date is None:

            streak.current_streak = 1

        elif streak.last_submission_date == today:

            pass

        elif streak.last_submission_date == today - timedelta(days=1):

            streak.current_streak += 1

        else:

            streak.current_streak = 1

        if streak.current_streak > streak.longest_streak:

            streak.longest_streak = streak.current_streak

        streak.last_submission_date = today

        streak.save()

        return render(

            request,

            "submission_result.html",

            {

                "problem": problem,
                "result": result,
                "ai_review": ai_review

            }

        )

    return render(

        request,

        "submit_solution.html",

        {

            "problem": problem

        }

    )


def submission_history(request):

    submissions = Submission.objects.filter(
        user=request.user
    ).order_by(
        "-submitted_at"
    )

    return render(

        request,

        "submission_history.html",

        {

            "submissions": submissions,
            "total_submissions":
            submissions.count()

        }

    )