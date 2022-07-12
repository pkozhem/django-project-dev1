from django.urls import path
from . import views


urlpatterns = [
    path('', views.AccountTemplateView.as_view(), name='account'),
]
