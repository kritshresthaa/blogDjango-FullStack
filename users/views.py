from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.


def register(request):
    if (request.method == "POST"):
        name = request.POST.get("user_name")
        f_name = request.POST.get("f_name")
        l_name = request.POST.get("l_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        c_password = request.POST.get("c_password")
        # print(name, f_name, l_name, email, password, c_password)
        if password == c_password:
            user = User.objects.create_user(
                username=name,
                email=email,
                first_name=f_name,
                last_name=l_name,
                password=password
            )
            user.save()
            return redirect("crud:home")
        else:
            print("Errror")

    return render(request, "users/register.html")


def loginUser(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST.get("user_name")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("crud:home")
            else:
                return redirect("users:signin")

    print(request.user)
    return render(request, "users/login.html")


@login_required
def logoutUser(request):
    logout(request)
    return redirect("crud:home")
