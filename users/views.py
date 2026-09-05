from django.shortcuts import render, redirect

from django.contrib.auth.models import User

from django.contrib.auth import (
    authenticate,
    login,
    logout
)

from submissions.models import Submission

from django.db.models import Avg


def register(request):

    if request.method == "POST":

        username = request.POST.get("username")

        email = request.POST.get("email")

        password = request.POST.get("password")

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect('/users/login/')

    return render(
        request,
        'register.html'
    )


def user_login(request):

    if request.method == "POST":

        username = request.POST.get("username")

        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(
                request,
                user
            )

            return redirect(
                '/dashboard/'
            )

        else:

            return render(
                request,
                'login.html',
                {
                    'error':
                    'Invalid username or password'
                }
            )

    return render(
        request,
        'login.html'
    )


def user_logout(request):

    logout(request)

    return render(
        request,
        'logout.html'
    )


def profile(request):

    submissions = Submission.objects.filter(
        user=request.user
    )

    context = {

        "submission_count":
        submissions.count(),

        "solved_count":
        submissions.values(
            'problem'
        ).distinct().count(),

        "average_score":
        submissions.aggregate(
            Avg('score')
        )['score__avg'] or 0

    }

    return render(
        request,
        'profile.html',
        context
    )