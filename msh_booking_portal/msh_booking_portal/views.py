from django.shortcuts import redirect

from allauth.account.views import LoginView, LogoutView


class LoginAllAuthView(LoginView):
    template_name = "login.html"

class LogoutAllAuthView(LogoutView):
    template_name = "login.html"