from django.contrib.auth.views import LoginView
from django.urls import path
from .views import ClienteRegisterView

urlpatterns = [
    path("register/", ClienteRegisterView.as_view(), name="register_cliente"),
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login")
]
