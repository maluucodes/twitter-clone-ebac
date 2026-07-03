from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from accounts.forms import ProfileForm, RegisterForm
from accounts.serializers import RegisterSerializer


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("feed")
    else:
        form = RegisterForm()

    return render(request, "accounts/register.html", {"form": form})


@login_required
def profile_view(request):
    return render(request, "accounts/profile.html")


@login_required
def edit_profile_view(request):
    profile = request.user.profile

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)

        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = ProfileForm(instance=profile)

    return render(request, "accounts/edit_profile.html", {"form": form})


@login_required
def delete_account_view(request):
    if request.method == "POST":
        user = request.user
        logout(request)
        user.delete()
        return redirect("register")

    return render(request, "accounts/delete_account.html")


@login_required
def users_list_view(request):
    users = User.objects.exclude(id=request.user.id)
    return render(request, "accounts/users_list.html", {"users": users})


@login_required
def user_profile_view(request, username):
    profile_user = get_object_or_404(User, username=username)
    return render(request, "accounts/user_profile.html", {"profile_user": profile_user})


@login_required
def follow_user_view(request, user_id):
    user_to_follow = get_object_or_404(User, id=user_id)
    request.user.profile.following.add(user_to_follow.profile)
    return redirect("users_list")


@login_required
def unfollow_user_view(request, user_id):
    user_to_unfollow = get_object_or_404(User, id=user_id)
    request.user.profile.following.remove(user_to_unfollow.profile)
    return redirect("users_list")


@login_required
def following_list_view(request):
    following = request.user.profile.following.all()
    return render(request, "accounts/following_list.html", {"following": following})


@login_required
def followers_list_view(request):
    followers = request.user.profile.followers.all()
    return render(request, "accounts/followers_list.html", {"followers": followers})


@login_required
def user_following_list_view(request, username):
    profile_user = get_object_or_404(User, username=username)
    following = profile_user.profile.following.all()

    return render(
        request,
        "accounts/user_following_list.html",
        {"profile_user": profile_user, "following": following},
    )


@login_required
def user_followers_list_view(request, username):
    profile_user = get_object_or_404(User, username=username)
    followers = profile_user.profile.followers.all()

    return render(
        request,
        "accounts/user_followers_list.html",
        {"profile_user": profile_user, "followers": followers},
    )


@api_view(["POST"])
def api_register_view(request):
    serializer = RegisterSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()

        return Response(
            {
                "id": user.id,
                "username": user.username,
                "email": user.email,
            },
            status=status.HTTP_201_CREATED,
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def api_login_view(request):
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(username=username, password=password)

    if user is not None:
        return Response(
            {
                "message": "Login realizado com sucesso.",
                "username": user.username,
            }
        )

    return Response(
        {"error": "Usuário ou senha inválidos."},
        status=status.HTTP_400_BAD_REQUEST,
    )
