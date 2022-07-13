from django.contrib.auth import get_user_model
from django.forms import ModelForm, TextInput

User = get_user_model()


class UserFormFix(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']
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
        }
