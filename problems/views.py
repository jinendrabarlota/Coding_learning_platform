from django.shortcuts import render, get_object_or_404

from .models import CodingProblem


def problem_list(request):

    problems = CodingProblem.objects.all()

    difficulty = request.GET.get(
        'difficulty'
    )

    search = request.GET.get(
        'search'
    )

    if difficulty:

        problems = problems.filter(
            difficulty=difficulty
        )

    if search:

        problems = problems.filter(
            title__icontains=search
        )

    return render(
        request,
        'problem_list.html',
        {
            'problems': problems
        }
    )


def problem_detail(request, problem_id):

    problem = get_object_or_404(
        CodingProblem,
        id=problem_id
    )

    return render(
        request,
        'problem_detail.html',
        {
            'problem': problem
        }
    )