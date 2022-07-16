from django.contrib.auth import get_user_model
from django.forms import ModelForm, TextInput, EmailInput, ImageField

User = get_user_model()


class UserFormFix(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'photo']
        widgets = {
            "username": TextInput(attrs={
                'class': 'form-control',
            }),
            "first_name": TextInput(attrs={
                'class': 'form-control',
            }),
            "last_name": TextInput(attrs={
                'class': 'form-control',
            }),
            "email": EmailInput(attrs={
                'class': 'form-control',
            }),
        }
