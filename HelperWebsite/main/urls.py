from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.home, name="home_page"),
    path("Contact/us/", views.contact_form, name="contact_page"),
    path("Contact/received//<contact_id>/", views.contact_received, name="contact_received"),

]