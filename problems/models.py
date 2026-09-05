from django.db import models


class CodingProblem(models.Model):

    DIFFICULTY_CHOICES = [

        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),

    ]

    title = models.CharField(
        max_length=200
    )

    difficulty = models.CharField(
        max_length=10,
        choices=DIFFICULTY_CHOICES
    )

    description = models.TextField()

    hint_1 = models.TextField(
        blank=True,
        null=True
    )

    hint_2 = models.TextField(
        blank=True,
        null=True
    )

    hint_3 = models.TextField(
        blank=True,
        null=True
    )

    sample_input = models.TextField(
        blank=True,
        null=True
    )

    sample_output = models.TextField(
        blank=True,
        null=True
    )

    test_cases = models.TextField(
        blank=True,
        null=True,
        help_text="""
Format:

input|output

Example:

hello|olleh
python|nohtyp
coding|gnidoc
"""
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.title