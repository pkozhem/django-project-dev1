from django.shortcuts import render
from django.views.generic import TemplateView


class AccountTemplateView(TemplateView):
    template_name = 'vcabinet/account.html'
