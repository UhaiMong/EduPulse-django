from django.contrib import admin
from .models import Tutor, Review

# Register your models here.


class TutorAdminSet(admin.ModelAdmin):
    list_display = ['fullname', 'age', 'tutor_phone',
                    'expert', 'lastEducation', 'image', 'short_bio', 'fee']


admin.site.register(Tutor, TutorAdminSet)
admin.site.register(Review)
