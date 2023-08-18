from django.urls import path
from .import views
app_name = "users"
urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.loginUser, name="signin"),
    path("logout/", views.logoutUser, name="signout")
]
