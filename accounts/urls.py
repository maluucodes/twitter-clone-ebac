from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeDoneView,
    PasswordChangeView,
)
from django.urls import path

from accounts.views import (
    api_login_view,
    api_register_view,
    delete_account_view,
    edit_profile_view,
    follow_user_view,
    followers_list_view,
    following_list_view,
    profile_view,
    register_view,
    unfollow_user_view,
    user_followers_list_view,
    user_following_list_view,
    user_profile_view,
    users_list_view,
)

urlpatterns = [
    path("cadastro/", register_view, name="register"),
    path(
        "login/",
        LoginView.as_view(template_name="accounts/login.html"),
        name="login",
    ),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("perfil/", profile_view, name="profile"),
    path("perfil/editar/", edit_profile_view, name="edit_profile"),
    path("usuarios/", users_list_view, name="users_list"),
    path(
        "usuarios/<int:user_id>/seguir/",
        follow_user_view,
        name="follow_user",
    ),
    path(
        "usuarios/<int:user_id>/deixar-de-seguir/",
        unfollow_user_view,
        name="unfollow_user",
    ),
    path(
        "senha/alterar/",
        PasswordChangeView.as_view(template_name="accounts/change_password.html"),
        name="change_password",
    ),
    path(
        "senha/alterada/",
        PasswordChangeDoneView.as_view(
            template_name="accounts/change_password_done.html"
        ),
        name="password_change_done",
    ),
    path("seguindo/", following_list_view, name="following_list"),
    path("seguidores/", followers_list_view, name="followers_list"),
    path("conta/deletar/", delete_account_view, name="delete_account"),
    path("api/register/", api_register_view, name="api_register"),
    path("api/login/", api_login_view, name="api_login"),
    path(
        "usuarios/<str:username>/seguindo/",
        user_following_list_view,
        name="user_following_list",
    ),
    path(
        "usuarios/<str:username>/seguidores/",
        user_followers_list_view,
        name="user_followers_list",
    ),
    path(
        "usuarios/<str:username>/",
        user_profile_view,
        name="user_profile",
    ),
]
