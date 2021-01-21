from datetime import timedelta

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    age = models.PositiveIntegerField(verbose_name='возраст')

    adctivation_key = models.CharField(max_length=128, blank=True, null=True)
    adctivation_key_expires = models.DateTimeField(default=now() + timedelta(hours=48))

    def is_activation_key_expired(self):
        if now() < self.adctivation_key_expires:
            return False
        return True


