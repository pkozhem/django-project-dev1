from django.contrib.auth import get_user_model
from django.views.generic import TemplateView

User = get_user_model()


class AccountTemplateView(TemplateView):
    template_name = 'vcabinet/account.html'
    model = User()


class ChangeInfo(TemplateView):
    template_name = 'vcabinet/change_info.html'
