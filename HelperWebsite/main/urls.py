from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.home, name="home_page"),
    path("Contact/us/", views.contact_form, name="contact_page"),
    path("Contact/received/<contact_id>/", views.contact_received, name="contact_received"),
    path("About/us/", views.about_us, name="about_us"),
    path("Travel/management/helper/", views.travel_management_helper, name="travel_management_helper"),
    path("Event/management/helper/", views.event_management_helper, name="event_management_helper"),
    path("Requests/for/help/", views.requests_for_help, name="requests_for_help"),
    path("Add/help/request/", views.add_help_request, name="add_help_request"),
    path("Update/help/request//<request_id>/", views.update_help_request, name="update_help_request"),
    path("Delete/help/request//<request_id>/", views.delete_help_request, name="delete_help_request"),
    path("Help/details//<request_id>/", views.help_details, name="help_details"),
    path("Join/us/", views.add_new_helper, name="add_new_helper"),
    path("Apply/<apply_id>/", views.apply, name="apply_page"),

]