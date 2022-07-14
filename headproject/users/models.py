from django.contrib.auth.models import AbstractUser
from autoslug import AutoSlugField


class User(AbstractUser):
    pass

    def instance(self):
        return self.username

    slug = AutoSlugField(populate_from=instance,
                         unique_with=['username', 'email'],
                         null=True,)

    def get_absolute_url(self):
        return f'/account/{self.slug}'
