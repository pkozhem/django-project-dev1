from django.forms import ModelForm, Textarea, TextInput
from .models import Articles, Comment


class ArticlesForm(ModelForm):

    class Meta:
        model = Articles
        fields = ['title', 'preview', 'content']
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title'
            }),
            "preview": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Preview'
            }),
            "content": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Text'
            })
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
