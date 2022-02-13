from django.shortcuts import redirect

from allauth.account.views import LoginView


class LoginAllAuthView(LoginView):
    template_name = "login.html"