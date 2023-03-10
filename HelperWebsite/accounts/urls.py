from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("sign/up/", views.sign_up, name="sign_up_user"),
    path("login/", views.login_user, name="login_user"),
    path("logout/", views.logout_user, name="logout_user"),
]