from django.contrib import admin
from . models import UserAccount

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name',
                    'user_phone', 'image', 'education']

    def first_name(self, obj):
        return obj.user.first_name

    def last_name(self, obj):
        return obj.user.last_name


class Applicants(admin.ModelAdmin):
    list_display = ['fullname', 'user_phone', 'approved']


admin.site.register(UserAccount, UserAdmin)
# admin.site.register(UserAccount, Applicants)
