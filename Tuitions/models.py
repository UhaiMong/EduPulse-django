from django.db import models
from . constants import EXPERT, STAR_CHOICE
from Users.models import UserAccount
from django.core.exceptions import ValidationError

# Create your models here.


class Tutor(models.Model):
    tutor = models.ManyToManyField(UserAccount)
    fullname = models.CharField(max_length=50)
    expert = models.CharField(max_length=20, choices=EXPERT)
    tutor_phone = models.CharField(max_length=12)
    image = models.ImageField(upload_to='tutor/images')
    lastEducation = models.CharField(max_length=40)
    short_bio = models.CharField(max_length=200)
    age = models.IntegerField()

    def clean(self):
        if self.age < 15 or self.age > 60:
            raise ValidationError("Age must be between 15 and 60.")
    fee = models.DecimalField(decimal_places=2, max_digits=12)

    def __str__(self):
        return f"{self.fullname} {self.age}"


class Review(models.Model):
    reviewer = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    review = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    rating = models.CharField(max_length=10, choices=STAR_CHOICE)

    def __str__(self):
        return f"{self.reviewer.user.first_name} reviewed to {self.tutor.fullname}"
