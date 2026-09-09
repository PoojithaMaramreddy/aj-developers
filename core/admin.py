from django.contrib import admin

from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "property_type",
        "location",
        "status",
        "created_at",
    )

    list_filter = (
        "property_type",
        "status",
    )

    search_fields = (
        "name",
        "location",
    )

    prepopulated_fields = {
        "slug": ("name",),
    }