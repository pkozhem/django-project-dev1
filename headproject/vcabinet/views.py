from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views.generic import TemplateView

User = get_user_model()


class AccountTemplateView(TemplateView):
    template_name = 'vcabinet/account.html'
