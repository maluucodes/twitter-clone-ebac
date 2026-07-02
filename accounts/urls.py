from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.urls import path

from accounts.views import edit_profile_view, profile_view, register_view


urlpatterns = [
    path("cadastro/", register_view, name="register"),
    path("login/", LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("perfil/", profile_view, name="profile"),
    path("perfil/editar/", edit_profile_view, name="edit_profile"),
    path(
    "senha/alterar/",
    PasswordChangeView.as_view(template_name="accounts/change_password.html"),
    name="change_password",
    ),
    path(
        "senha/alterada/",
        PasswordChangeDoneView.as_view(template_name="accounts/change_password_done.html"),
        name="password_change_done",
    ),
]