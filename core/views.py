from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse

from .models import (
    Project,
    Lead,
    SiteVisit,
    BookingRequest,
)


def home(request):
    projects = (
        Project.objects
        .filter(status="PUBLISHED")
        .order_by("-created_at")
    )

    return render(
        request,
        "core/home.html",
        {"projects": projects},
    )


def project_list(request):
    projects = (
        Project.objects
        .filter(status="PUBLISHED")
        .order_by("-created_at")
    )

    return render(
        request,
        "core/projects.html",
        {"projects": projects},
    )


def project_detail(request, slug):
    project = get_object_or_404(
        Project.objects.prefetch_related(
            "images",
            "videos",
            "amenities",
            "approvals",
            "plots",
        ),
        slug=slug,
        status="PUBLISHED",
    )

    return render(
        request,
        "core/project_detail.html",
        {"project": project},
    )


def project_enquiry(request, slug):

    project = get_object_or_404(
        Project,
        slug=slug,
        status="PUBLISHED",
    )

    if request.method == "POST":

        name = request.POST.get(
            "name",
            "",
        ).strip()

        phone = request.POST.get(
            "phone",
            "",
        ).strip()

        email = request.POST.get(
            "email",
            "",
        ).strip()

        interested_plot_id = request.POST.get(
            "interested_plot",
            "",
        ).strip()

        message = request.POST.get(
            "message",
            "",
        ).strip()

        whatsapp_opt_in = (
            request.POST.get("whatsapp_opt_in") == "on"
        )

        # Basic validation
        if not name or not phone:

            return render(
                request,
                "core/project_detail.html",
                {
                    "project": project,
                    "enquiry_error":
                        "Please enter your name and phone number.",
                },
            )

        interested_plot = None

        if interested_plot_id:

            interested_plot = (
                project.plots
                .filter(id=interested_plot_id)
                .first()
            )

        # Find existing lead using phone + project
        lead = (
            Lead.objects
            .filter(
                phone=phone,
                interested_project=project,
            )
            .order_by("-created_at")
            .first()
        )

        if not lead:

            # Create a new lead
            Lead.objects.create(
                name=name,
                phone=phone,
                email=email,
                source="WEBSITE",
                interested_project=project,
                interested_plot=interested_plot,
                message=message,
                status="NEW",
                whatsapp_opt_in=whatsapp_opt_in,
            )

        else:

            # Existing lead:
            # DO NOT change the existing name.

            if email and not lead.email:
                lead.email = email

            if interested_plot:
                lead.interested_plot = interested_plot

            if message:
                lead.message = message

            if whatsapp_opt_in:
                lead.whatsapp_opt_in = True

            # Do not reset existing lead status.
            lead.save()

        return redirect(
            f"{reverse('project_detail', args=[project.slug])}"
            "?enquiry=success"
        )

    return redirect(
        "project_detail",
        slug=project.slug,
    )


def project_site_visit(request, slug):

    project = get_object_or_404(
        Project,
        slug=slug,
        status="PUBLISHED",
    )

    if request.method == "POST":

        name = request.POST.get(
            "name",
            "",
        ).strip()

        phone = request.POST.get(
            "phone",
            "",
        ).strip()

        email = request.POST.get(
            "email",
            "",
        ).strip()

        preferred_date = request.POST.get(
            "preferred_date",
            "",
        ).strip()

        preferred_time = request.POST.get(
            "preferred_time",
            "",
        ).strip()

        message = request.POST.get(
            "message",
            "",
        ).strip()

        # Basic validation
        if not name or not phone or not preferred_date:

            return render(
                request,
                "core/project_detail.html",
                {
                    "project": project,
                    "site_visit_error":
                        "Please enter your name, phone number and preferred date.",
                },
            )

        # Find existing lead using phone + project
        lead = (
            Lead.objects
            .filter(
                phone=phone,
                interested_project=project,
            )
            .order_by("-created_at")
            .first()
        )

        if not lead:

            # Create a new lead
            lead = Lead.objects.create(
                name=name,
                phone=phone,
                email=email,
                source="WEBSITE",
                interested_project=project,
                status="SITE_VISIT_SCHEDULED",
                message=message,
            )

        else:

            # Existing lead:
            # DO NOT change the existing name.

            if email and not lead.email:
                lead.email = email

            if message:
                lead.message = message

            lead.status = "SITE_VISIT_SCHEDULED"

            lead.save()

        # Create site visit against the existing lead
        SiteVisit.objects.create(
            lead=lead,
            project=project,
            preferred_date=preferred_date,
            preferred_time=preferred_time,
            message=message,
            status="REQUESTED",
        )

        return redirect(
            f"{reverse('project_detail', args=[project.slug])}"
            "?site_visit=success"
        )

    return redirect(
        "project_detail",
        slug=project.slug,
    )


def project_booking_request(request, slug):

    project = get_object_or_404(
        Project,
        slug=slug,
        status="PUBLISHED",
    )

    if request.method == "POST":

        name = request.POST.get(
            "name",
            "",
        ).strip()

        phone = request.POST.get(
            "phone",
            "",
        ).strip()

        email = request.POST.get(
            "email",
            "",
        ).strip()

        message = request.POST.get(
            "message",
            "",
        ).strip()

        # Basic validation
        if not name or not phone:

            return render(
                request,
                "core/project_detail.html",
                {
                    "project": project,
                    "booking_error":
                        "Please enter your name and phone number.",
                },
            )

        # Find existing lead using phone + project
        lead = (
            Lead.objects
            .filter(
                phone=phone,
                interested_project=project,
            )
            .order_by("-created_at")
            .first()
        )

        if not lead:

            # Create a new lead
            lead = Lead.objects.create(
                name=name,
                phone=phone,
                email=email,
                source="WEBSITE",
                interested_project=project,
                message=message,
                status="BOOKING_REQUESTED",
            )

        else:

            # Existing lead:
            # DO NOT change the existing name.

            if email and not lead.email:
                lead.email = email

            if message:
                lead.message = message

            lead.status = "BOOKING_REQUESTED"

            lead.save()

        # Check whether this lead already has a booking request
        existing_booking = (
            BookingRequest.objects
            .filter(
                lead=lead,
                project=project,
            )
            .first()
        )

        if existing_booking:

            return redirect(
                f"{reverse('project_detail', args=[project.slug])}"
                "?booking=already_requested"
            )

        # Create booking request
        BookingRequest.objects.create(
            lead=lead,
            project=project,
            message=message,
        )

        return redirect(
            f"{reverse('project_detail', args=[project.slug])}"
            "?booking=success"
        )

    return redirect(
        "project_detail",
        slug=project.slug,
    )