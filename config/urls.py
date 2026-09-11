from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from core import views


urlpatterns = [
    path("admin/", admin.site.urls),

    path(
        "",
        views.home,
        name="home",
    ),

    path(
        "projects/",
        views.project_list,
        name="projects",
    ),

    path(
        "projects/<slug:slug>/enquiry/",
        views.project_enquiry,
        name="project_enquiry",
    ),

    path(
        "projects/<slug:slug>/site-visit/",
        views.project_site_visit,
        name="project_site_visit",
    ),

    path(
        "projects/<slug:slug>/booking-request/",
        views.project_booking_request,
        name="project_booking_request",
    ),


    path(
        "projects/<slug:slug>/",
        views.project_detail,
        name="project_detail",
    ),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )