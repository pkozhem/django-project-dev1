from django.contrib.auth.models import AbstractUser
from autoslug import AutoSlugField
from django.db import models


class User(AbstractUser):
    pass


class Profile(models.Model):
    def instance(self):
        return f'{self.user.username}'

    def __str__(self):
        return f'{self.user.username} Profile'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField('bio', blank=True, null=True, default=' ')
    image = models.ImageField(default='default.png', blank=True, upload_to='profile_pic')
    slug = AutoSlugField(populate_from=instance,
                         unique_with=['user'],
                         null=True)
