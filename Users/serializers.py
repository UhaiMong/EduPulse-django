from rest_framework import serializers
from . models import UserAccount
from django.contrib.auth.models import User


class Applicants(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = '__all__'


class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password', 'confirm_password']

    def save(self):
        username = self.validated_data['username']
        email = self.validated_data['email']
        password1 = self.validated_data['password']
        password2 = self.validated_data['confirm_password']

        if password1 != password2:
            raise serializers.ValidationError(
                {'error': "Password doesn't matched"})
        if User.objects.filter(email=email).exists() | User.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                {'error': "Email or username already exist"})
        account = User(username=username, email=email)
        print(account)
        account.set_password(password1)
        account.is_active = False
        account.save()
        return account
