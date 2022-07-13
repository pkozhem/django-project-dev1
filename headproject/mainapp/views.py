from django.contrib.auth import get_user_model
from django.shortcuts import render


def index(request):
    return render(request, 'mainapp/index.html')


def about(request):
    d = {
        'values': ['Hello', 'everybody!']
    }
    return render(request, 'mainapp/about.html', d)
