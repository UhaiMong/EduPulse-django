from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from .constants import EDUCATION
from Tuitions.models import Tutor

# Create your models here.


class UserAccount(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE)
    education = models.CharField(max_length=10, choices=EDUCATION)
    user_phone = models.CharField(max_length=12)
    image = models.ImageField(upload_to='users/images/')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Application(models.Model):
    applicant = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Applicant: {self.applicant.user.first_name} for the Tutor: {self.tutor.fullname}"
