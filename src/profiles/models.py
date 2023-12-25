from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
from django.db import models
# Create your models here.

user_model = get_user_model()


class UserProfile(models.Model):
    UserProfileId = models.BigAutoField(
        _('Id'),
        primary_key=True
    )
    user = models.OneToOneField(
        user_model,
        on_delete=models.CASCADE,
        related_name='Profile',
    )
    Picture = models.FileField(
        _('Picture'),
        null=True,
        blank=True,
        max_length=300,
        upload_to='uploads/user_profiles'
    )

