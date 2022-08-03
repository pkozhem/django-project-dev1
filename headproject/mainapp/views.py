from django.views.generic import TemplateView


class HomePage(TemplateView):
    """View for the Home page"""
    template_name = 'mainapp/index.html'


class AboutPage(TemplateView):
    """View for the Home page"""
    template_name = 'mainapp/about.html'
