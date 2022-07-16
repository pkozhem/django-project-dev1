from django.contrib.auth.models import AbstractUser
from autoslug import AutoSlugField
from django.db import models


class User(AbstractUser):
    pass

    def instance(self):
        return self.username

    slug = AutoSlugField(populate_from=instance,
                         unique_with=['username', 'email'],
                         null=True,)
    photo = models.ImageField('photo', default='default.png', blank=True, upload_to='users/')

    def get_absolute_url(self):
        return f'/account/{self.slug}'
