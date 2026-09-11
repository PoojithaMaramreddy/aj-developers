from django.contrib import admin

from .models import (
    Project,
    ProjectImage,
    ProjectVideo,
    Amenity,
    ProjectApproval,
    Plot,
    Lead,
    SiteVisit,
    BookingRequest,
    SalesAgent,
    LeadFollowUp,
    Campaign,
    CampaignRecipient,
)

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 0
    fields = ("image", "title", "caption", "display_order")
    readonly_fields = ("created_at",)
    ordering = ("display_order",)


class ProjectVideoInline(admin.TabularInline):
    model = ProjectVideo
    extra = 0
    fields = ("title", "youtube_url", "description", "display_order")
    readonly_fields = ("created_at",)
    ordering = ("display_order",)


class AmenityInline(admin.TabularInline):
    model = Amenity
    extra = 0
    fields = ("name", "description", "display_order")
    readonly_fields = ("created_at",)
    ordering = ("display_order",)


class ProjectApprovalInline(admin.TabularInline):
    model = ProjectApproval
    extra = 0
    fields = (
        "approval_type",
        "approval_number",
        "authority",
        "document",
        "description",
        "display_order",
    )
    readonly_fields = ("created_at",)
    ordering = ("display_order",)


class PlotInline(admin.TabularInline):
    model = Plot
    extra = 0
    fields = (
        "plot_number",
        "plot_size",
        "dimension",
        "facing",
        "block",
        "layout_position",
    )
    readonly_fields = ("created_at",)
    ordering = ("plot_number",)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "property_type",
        "location",
        "status",
        "created_at",
    )
    list_filter = ("property_type", "status")
    search_fields = ("name", "location", "slug")
    readonly_fields = ("created_at", "updated_at")
    prepopulated_fields = {"slug": ("name",)}

    inlines = [
        ProjectImageInline,
        ProjectVideoInline,
        AmenityInline,
        ProjectApprovalInline,
        PlotInline,
    ]


@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = (
        "project",
        "title",
        "display_order",
        "created_at",
    )
    list_filter = ("project",)
    search_fields = ("project__name", "title", "caption")
    readonly_fields = ("created_at",)
    list_select_related = ("project",)


@admin.register(ProjectVideo)
class ProjectVideoAdmin(admin.ModelAdmin):
    list_display = (
        "project",
        "title",
        "display_order",
        "created_at",
    )
    list_filter = ("project",)
    search_fields = ("project__name", "title")
    readonly_fields = ("created_at",)
    list_select_related = ("project",)


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = (
        "project",
        "name",
        "display_order",
        "created_at",
    )
    list_filter = ("project",)
    search_fields = ("project__name", "name", "description")
    readonly_fields = ("created_at",)
    list_select_related = ("project",)


@admin.register(ProjectApproval)
class ProjectApprovalAdmin(admin.ModelAdmin):
    list_display = (
        "project",
        "approval_type",
        "approval_number",
        "authority",
        "display_order",
    )
    list_filter = ("project", "authority")
    search_fields = (
        "project__name",
        "approval_type",
        "approval_number",
        "authority",
    )
    readonly_fields = ("created_at",)
    list_select_related = ("project",)


@admin.register(Plot)
class PlotAdmin(admin.ModelAdmin):
    list_display = (
        "project",
        "plot_number",
        "plot_size",
        "dimension",
        "facing",
        "block",
    )
    list_filter = ("project", "facing", "block")
    search_fields = (
        "project__name",
        "plot_number",
        "plot_size",
        "facing",
    )
    readonly_fields = ("created_at",)
    list_select_related = ("project",)

class SiteVisitInline(admin.TabularInline):
    model = SiteVisit
    extra = 0
    readonly_fields = ("created_at", "updated_at")


class BookingRequestInline(admin.TabularInline):
    model = BookingRequest
    extra = 0
    readonly_fields = ("created_at", "updated_at")


class LeadFollowUpInline(admin.TabularInline):
    model = LeadFollowUp
    extra = 0
    readonly_fields = ("created_at",)

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "phone",
        "interested_project",
        "interested_plot",
        "source",
        "status",
        "whatsapp_opt_in",
        "created_at",
    )

    list_filter = (
        "source",
        "status",
        "whatsapp_opt_in",
    )

    search_fields = (
        "name",
        "phone",
        "email",
        "interested_project__name",
        "interested_plot__plot_number",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    list_select_related = (
        "interested_project",
        "interested_plot",
    )

    inlines = [
        SiteVisitInline,
        BookingRequestInline,
        LeadFollowUpInline,
    ]


@admin.register(SiteVisit)
class SiteVisitAdmin(admin.ModelAdmin):
    list_display = (
        "lead",
        "project",
        "preferred_date",
        "preferred_time",
        "status",
        "created_at",
    )
    list_filter = (
        "status",
        "preferred_date",
        "project",
    )
    search_fields = (
        "lead__name",
        "lead__phone",
        "project__name",
    )
    readonly_fields = ("created_at", "updated_at")
    list_select_related = ("lead", "project")


@admin.register(BookingRequest)
class BookingRequestAdmin(admin.ModelAdmin):
    list_display = (
        "lead",
        "project",
        "plot",
        "status",
        "created_at",
    )
    list_filter = (
        "status",
        "project",
    )
    search_fields = (
        "lead__name",
        "lead__phone",
        "project__name",
        "plot__plot_number",
    )
    readonly_fields = ("created_at", "updated_at")
    list_select_related = ("lead", "project", "plot")


@admin.register(SalesAgent)
class SalesAgentAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "phone",
        "email",
        "active",
        "created_at",
    )
    list_filter = ("active",)
    search_fields = ("name", "phone", "email")
    readonly_fields = ("created_at",)


@admin.register(LeadFollowUp)
class LeadFollowUpAdmin(admin.ModelAdmin):
    list_display = (
        "lead",
        "sales_agent",
        "follow_up_date",
        "follow_up_type",
        "status",
    )
    list_filter = (
        "follow_up_type",
        "status",
        "sales_agent",
    )
    search_fields = (
        "lead__name",
        "lead__phone",
        "sales_agent__name",
        "notes",
    )
    readonly_fields = ("created_at",)
    list_select_related = ("lead", "sales_agent")


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "campaign_type",
        "scheduled_at",
        "status",
        "created_at",
    )
    list_filter = (
        "campaign_type",
        "status",
    )
    search_fields = ("name", "message_template")
    readonly_fields = ("created_at", "updated_at")


@admin.register(CampaignRecipient)
class CampaignRecipientAdmin(admin.ModelAdmin):
    list_display = (
        "campaign",
        "lead",
        "status",
        "sent_at",
        "created_at",
    )
    list_filter = (
        "status",
        "campaign",
    )
    search_fields = (
        "campaign__name",
        "lead__name",
        "lead__phone",
    )
    readonly_fields = ("created_at",)
    list_select_related = ("campaign", "lead")
