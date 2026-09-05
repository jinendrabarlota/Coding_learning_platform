from django.urls import path
from . import views

urlpatterns = [

    path(
        "run/",
        views.run_code,
        name="run_code"
    ),

    path(
        "history/",
        views.submission_history,
        name="submission_history"
    ),

    path(
        "<int:problem_id>/",
        views.submit_solution,
        name="submit_solution"
    ),

]