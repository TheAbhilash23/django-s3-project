from django.contrib import admin
from profiles import models
# Register your models here.


@admin.register(models.UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'Picture',
        'UserProfileId',
    )
