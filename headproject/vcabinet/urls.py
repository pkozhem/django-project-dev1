from django.urls import path
from . import views


urlpatterns = [
    path('<slug>', views.AccountTemplateView.as_view(), name='account'),
    path('<slug>/change_info', views.ChangeInfo.as_view(), name='change_info'),
]
