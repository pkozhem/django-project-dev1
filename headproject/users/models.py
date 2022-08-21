from autoslug.utils import slugify
from django.contrib.auth.models import AbstractUser
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
    slug = models.SlugField(unique=True, default='')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user)
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
