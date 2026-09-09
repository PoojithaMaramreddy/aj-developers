from django.db import models


class Project(models.Model):
    PROPERTY_TYPES = [
        ("OPEN_PLOT", "Open Plot"),
        ("VILLA", "Villa"),
        ("APARTMENT", "Apartment"),
        ("COMMERCIAL", "Commercial Space"),
        ("OTHER", "Other"),
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
    amenities = models.TextField(blank=True)

    google_maps_url = models.URLField(blank=True)

    status = models.CharField(
        max_length=20,
        choices=[
            ("DRAFT", "Draft"),
            ("PUBLISHED", "Published"),
            ("ARCHIVED", "Archived"),
        ],
        default="DRAFT",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name