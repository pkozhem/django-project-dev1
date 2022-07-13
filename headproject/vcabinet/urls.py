from django.urls import path
from . import views


urlpatterns = [
    path('', views.AccountTemplateView.as_view(), name='account'),
    path('<int:pk>/change_info', views.ChangeInfo.as_view(), name='change_info'),
]
