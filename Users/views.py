from django.shortcuts import render
from django.views.generic import TemplateView, View

# Create your views here.


class ProfileView(TemplateView):
    template_name = 'profile.html'


class RegisterView(TemplateView):
    template_name = 'register.html'


class LoginView(TemplateView):
    template_name = 'login.html'
