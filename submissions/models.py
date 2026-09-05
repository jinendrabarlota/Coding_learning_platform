from django.db import models
from django.contrib.auth.models import User
from problems.models import CodingProblem


class Submission(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    problem = models.ForeignKey(
        CodingProblem,
        on_delete=models.CASCADE
    )

    code = models.TextField()

    language = models.CharField(
        max_length=50,
        default='python'
    )

    status = models.CharField(
        max_length=50,
        default='Pending'
    )

    score = models.IntegerField(
        default=0
    )

    runtime = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    memory = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    submitted_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.problem.title}"