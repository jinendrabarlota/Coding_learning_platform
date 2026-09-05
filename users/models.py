from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    bio = models.TextField(
        blank=True
    )

    def __str__(self):
        return self.user.username


class UserStreak(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    current_streak = models.IntegerField(
        default=0
    )

    longest_streak = models.IntegerField(
        default=0
    )

    last_submission_date = models.DateField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.user.username