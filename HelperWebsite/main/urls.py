from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.home, name="home_page"),
    path("Contact/us/", views.contact_form, name="contact_page"),
    path("Contact/received//<contact_id>/", views.contact_received, name="contact_received"),
    path("About/us/", views.about_us, name="about_us"),
    path("Travel/management/helper", views.travel_management_helper, name="travel_management_helper"),
    path("Event/management/helper", views.event_management_helper, name="event_management_helper"),

]