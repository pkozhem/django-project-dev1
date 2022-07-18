from django.contrib.auth.models import AbstractUser
from autoslug import AutoSlugField
from django.db import models
from PIL import Image


class User(AbstractUser):
    pass


class Profile(models.Model):
    def __str__(self):
        return f'{self.user.username}'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField('bio', blank=True, null=True, default=' ')
    image = models.ImageField(default='default.png', blank=True, upload_to='profile_pic')
    slug = AutoSlugField(populate_from=__str__,
                         unique_with=['user'],
                         null=True)

    def save(self, **kwargs):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
