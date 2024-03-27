from django.shortcuts import render
from django.views.generic import TemplateView, View
from .import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes

# Create your views here.


class ProfileView(TemplateView):
    template_name = 'profile.html'


class RegisterView(APIView):
    serializers_class = serializers.RegistrationSerializer

    def post(self, request):
        serializer = self.serializers_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            print(user)
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            return Response("Successfully Registered. Check your mail to verify.")
        return Response("Successfully Registered. Check your mail to verify.")


class LoginView(TemplateView):
    template_name = 'login.html'
