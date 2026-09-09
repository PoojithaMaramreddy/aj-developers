from django.contrib import admin

from .models import Project, ProjectImage, ProjectVideo


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


@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = (
        "project",
        "title",
        "display_order",
        "created_at",
    )

    list_filter = (
        "project",
    )

    search_fields = (
        "project__name",
        "title",
        "caption",
    )

    ordering = (
        "project",
        "display_order",
    )


@admin.register(ProjectVideo)
class ProjectVideoAdmin(admin.ModelAdmin):
    list_display = (
        "project",
        "title",
        "display_order",
        "created_at",
    )

    list_filter = (
        "project",
    )

    search_fields = (
        "project__name",
        "title",
        "description",
    )

    ordering = (
        "project",
        "display_order",
    )