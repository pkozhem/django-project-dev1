from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

    def get_absolute_url(self):
        return f'/account'
