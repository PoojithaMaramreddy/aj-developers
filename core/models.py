from django.db import models


class Project(models.Model):
    PROPERTY_TYPES = [
        ("OPEN_PLOT", "Open Plot"),
        ("VILLA", "Villa"),
        ("APARTMENT", "Apartment"),
        ("COMMERCIAL", "Commercial Space"),
        ("OTHER", "Other"),
    ]

    STATUS_CHOICES = [
        ("DRAFT", "Draft"),
        ("PUBLISHED", "Published"),
        ("ARCHIVED", "Archived"),
    ]

    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    property_type = models.CharField(
        max_length=20,
        choices=PROPERTY_TYPES,
        default="OPEN_PLOT",
    )

    location = models.CharField(max_length=200)
    location_description = models.TextField(blank=True)

    total_area = models.CharField(max_length=100, blank=True)
    total_plots = models.PositiveIntegerField(null=True, blank=True)

    description = models.TextField()
    highlights = models.TextField(blank=True)

    developer_name = models.CharField(max_length=200, blank=True)
    promoter_name = models.CharField(max_length=200, blank=True)

    google_maps_url = models.URLField(blank=True)

    brochure = models.FileField(
        upload_to="projects/brochures/",
        blank=True,
        null=True,
    )

    layout_image = models.ImageField(
        upload_to="projects/layouts/",
        blank=True,
        null=True,
    )

    layout_pdf = models.FileField(
        upload_to="projects/layouts/",
        blank=True,
        null=True,
    )

    seo_title = models.CharField(max_length=200, blank=True)

    meta_description = models.TextField(blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="DRAFT",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name

class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="images",
    )

    image = models.ImageField(
        upload_to="projects/images/",
    )

    title = models.CharField(
        max_length=200,
        blank=True,
    )

    caption = models.TextField(
        blank=True,
    )

    display_order = models.PositiveIntegerField(
        default=0,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ["display_order", "-created_at"]

    def __str__(self):
        return f"{self.project.name} - {self.title or 'Image'}"

class ProjectVideo(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="videos",
    )

    title = models.CharField(
        max_length=200,
        blank=True,
    )

    youtube_url = models.URLField()

    description = models.TextField(
        blank=True,
    )

    display_order = models.PositiveIntegerField(
        default=0,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ["display_order", "-created_at"]

    def __str__(self):
        return f"{self.project.name} - {self.title or 'Video'}"

class Amenity(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="amenities",
    )

    name = models.CharField(max_length=200)

    description = models.TextField(
        blank=True,
    )

    display_order = models.PositiveIntegerField(
        default=0,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ["display_order", "-created_at"]

    def __str__(self):
        return f"{self.project.name} - {self.name}"

class ProjectApproval(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="approvals",
    )

    approval_type = models.CharField(
        max_length=200,
    )

    approval_number = models.CharField(
        max_length=200,
        blank=True,
    )

    authority = models.CharField(
        max_length=200,
        blank=True,
    )

    document = models.FileField(
        upload_to="projects/approvals/",
        blank=True,
        null=True,
    )

    description = models.TextField(
        blank=True,
    )

    display_order = models.PositiveIntegerField(
        default=0,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ["display_order", "-created_at"]

    def __str__(self):
        return f"{self.project.name} - {self.approval_type}"

class Plot(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="plots",
    )

    plot_number = models.CharField(
        max_length=50,
    )

    plot_size = models.CharField(
        max_length=100,
        blank=True,
    )

    dimension = models.CharField(
        max_length=100,
        blank=True,
    )

    facing = models.CharField(
        max_length=50,
        blank=True,
    )

    block = models.CharField(
        max_length=50,
        blank=True,
    )

    layout_position = models.CharField(
        max_length=100,
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ["plot_number"]

    def __str__(self):
        return f"{self.project.name} - Plot {self.plot_number}"

class Lead(models.Model):
    STATUS_CHOICES = [
        ("NEW", "New"),
        ("CONTACTED", "Contacted"),
        ("INTERESTED", "Interested"),
        ("SITE_VISIT_SCHEDULED", "Site Visit Scheduled"),
        ("SITE_VISIT_DONE", "Site Visit Done"),
        ("BOOKING_REQUESTED", "Booking Requested"),
        ("BOOKED", "Booked"),
        ("CLOSED", "Closed"),
        ("NOT_INTERESTED", "Not Interested"),
    ]

    SOURCE_CHOICES = [
        ("WEBSITE", "Website"),
        ("WHATSAPP", "WhatsApp"),
        ("INSTAGRAM", "Instagram"),
        ("FACEBOOK", "Facebook"),
        ("YOUTUBE", "YouTube"),
        ("GOOGLE", "Google"),
        ("PHONE", "Phone"),
        ("OTHER", "Other"),
    ]

    name = models.CharField(
        max_length=200,
    )

    phone = models.CharField(
        max_length=20,
    )

    email = models.EmailField(
        blank=True,
    )

    interested_project = models.ForeignKey(
        Project,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="leads",
    )

    interested_plot = models.ForeignKey(
        Plot,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="leads",
    )

    message = models.TextField(
        blank=True,
    )

    source = models.CharField(
        max_length=20,
        choices=SOURCE_CHOICES,
        default="WEBSITE",
    )

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default="NEW",
    )

    whatsapp_opt_in = models.BooleanField(
        default=False,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.phone}"

class SiteVisit(models.Model):
    STATUS_CHOICES = [
        ("REQUESTED", "Requested"),
        ("CONFIRMED", "Confirmed"),
        ("COMPLETED", "Completed"),
        ("CANCELLED", "Cancelled"),
        ("RESCHEDULED", "Rescheduled"),
    ]

    lead = models.ForeignKey(
        Lead,
        on_delete=models.CASCADE,
        related_name="site_visits",
    )

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="site_visits",
    )

    preferred_date = models.DateField()

    preferred_time = models.TimeField(
        null=True,
        blank=True,
    )

    message = models.TextField(
        blank=True,
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="REQUESTED",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ["preferred_date", "preferred_time"]

    def __str__(self):
        return f"{self.lead.name} - {self.project.name} - {self.preferred_date}"

class BookingRequest(models.Model):
    STATUS_CHOICES = [
        ("REQUESTED", "Requested"),
        ("CONTACTED", "Contacted"),
        ("UNDER_PROCESS", "Under Process"),
        ("CONFIRMED", "Confirmed"),
        ("CANCELLED", "Cancelled"),
    ]

    lead = models.ForeignKey(
        Lead,
        on_delete=models.CASCADE,
        related_name="booking_requests",
    )

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="booking_requests",
    )

    plot = models.ForeignKey(
        Plot,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="booking_requests",
    )

    message = models.TextField(
        blank=True,
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="REQUESTED",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.lead.name} - {self.project.name}"

class SalesAgent(models.Model):
    name = models.CharField(
        max_length=200,
    )

    phone = models.CharField(
        max_length=20,
    )

    email = models.EmailField(
        blank=True,
    )

    active = models.BooleanField(
        default=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.name

class LeadFollowUp(models.Model):
    FOLLOW_UP_TYPES = [
        ("CALL", "Call"),
        ("WHATSAPP", "WhatsApp"),
        ("SITE_VISIT", "Site Visit"),
        ("EMAIL", "Email"),
        ("OTHER", "Other"),
    ]

    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("COMPLETED", "Completed"),
        ("CANCELLED", "Cancelled"),
    ]

    lead = models.ForeignKey(
        Lead,
        on_delete=models.CASCADE,
        related_name="follow_ups",
    )

    sales_agent = models.ForeignKey(
        SalesAgent,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="follow_ups",
    )

    follow_up_date = models.DateTimeField()

    follow_up_type = models.CharField(
        max_length=20,
        choices=FOLLOW_UP_TYPES,
        default="CALL",
    )

    notes = models.TextField(
        blank=True,
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="PENDING",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ["follow_up_date"]

    def __str__(self):
        return f"{self.lead.name} - {self.follow_up_date}"

class Campaign(models.Model):
    CAMPAIGN_TYPES = [
        ("NEW_PROJECT", "New Project Launch"),
        ("PROJECT_UPDATE", "Project Update"),
        ("SITE_VISIT", "Site Visit Invite"),
        ("VIDEO_UPDATE", "New Video"),
        ("OFFER", "Offer"),
        ("FOLLOW_UP", "Follow-up"),
        ("OTHER", "Other"),
    ]

    STATUS_CHOICES = [
        ("DRAFT", "Draft"),
        ("SCHEDULED", "Scheduled"),
        ("RUNNING", "Running"),
        ("COMPLETED", "Completed"),
        ("CANCELLED", "Cancelled"),
    ]

    name = models.CharField(
        max_length=200,
    )

    message_template = models.TextField()

    campaign_type = models.CharField(
        max_length=30,
        choices=CAMPAIGN_TYPES,
        default="PROJECT_UPDATE",
    )

    scheduled_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="DRAFT",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name

class CampaignRecipient(models.Model):
    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("SENT", "Sent"),
        ("FAILED", "Failed"),
        ("SKIPPED", "Skipped"),
    ]

    campaign = models.ForeignKey(
        Campaign,
        on_delete=models.CASCADE,
        related_name="recipients",
    )

    lead = models.ForeignKey(
        Lead,
        on_delete=models.CASCADE,
        related_name="campaign_recipients",
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="PENDING",
    )

    sent_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ["-created_at"]
        constraints = [
            models.UniqueConstraint(
                fields=["campaign", "lead"],
                name="unique_campaign_lead",
            ),
        ]

    def __str__(self):
        return f"{self.campaign.name} - {self.lead.name}"