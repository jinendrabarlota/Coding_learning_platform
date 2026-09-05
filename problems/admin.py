from django.contrib import admin
from .models import CodingProblem


@admin.register(CodingProblem)
class CodingProblemAdmin(admin.ModelAdmin):

    list_display = (

        "title",

        "difficulty",

        "created_at"

    )

    list_filter = (

        "difficulty",

    )

    search_fields = (

        "title",

        "description"

    )