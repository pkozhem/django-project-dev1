from django.shortcuts import render
from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = 'mainapp/index.html'


def about(request):
    d = {
        'values': ['Hello', 'everybody!']
    }
    return render(request, 'mainapp/about.html', d)
