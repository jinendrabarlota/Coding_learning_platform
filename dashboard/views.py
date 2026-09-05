from django.shortcuts import render
from submissions.models import Submission
from users.models import UserStreak


def home(request):

    return render(
        request,
        "home.html"
    )


def dashboard(request):

    accepted = Submission.objects.filter(
        user=request.user,
        status="Accepted"
    )

    all_submissions = Submission.objects.filter(
        user=request.user
    )

    solved_count = accepted.values(
        "problem"
    ).distinct().count()

    total_submissions = all_submissions.count()

    acceptance_rate = 0

    if total_submissions > 0:

        acceptance_rate = round(
            (accepted.count() / total_submissions) * 100,
            2
        )

    easy_count = accepted.filter(
        problem__difficulty="Easy"
    ).values(
        "problem"
    ).distinct().count()

    medium_count = accepted.filter(
        problem__difficulty="Medium"
    ).values(
        "problem"
    ).distinct().count()

    hard_count = accepted.filter(
        problem__difficulty="Hard"
    ).values(
        "problem"
    ).distinct().count()

    if solved_count >= 100:

        badge = "💎 Rift Master"

    elif solved_count >= 50:

        badge = "🥇 Advanced Solver"

    elif solved_count >= 25:

        badge = "🥈 Intermediate Solver"

    elif solved_count >= 5:

        badge = "🥉 Beginner Solver"

    else:

        badge = "🌱 New Coder"

    streak, created = UserStreak.objects.get_or_create(
        user=request.user
    )

    context = {

        "solved_count": solved_count,
        "total_submissions": total_submissions,
        "acceptance_rate": acceptance_rate,

        "easy_count": easy_count,
        "medium_count": medium_count,
        "hard_count": hard_count,

        "badge": badge,

        "current_streak": streak.current_streak,
        "longest_streak": streak.longest_streak,

    }

    return render(
        request,
        "dashboard.html",
        context
    )


def leaderboard(request):

    return render(
        request,
        "leaderboard.html"
    )