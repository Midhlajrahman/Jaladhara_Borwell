from django.urls import path

from . import views

app_name = "web"
urlpatterns = [
    path("", views.index, name="index"),
    path("about-us/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path("contact/", views.contact, name="contact"),
    path("service_details/<slug>/", views.service_details, name="service_details"),
    path("projects",views.projects,name="projects")
]
