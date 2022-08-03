from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('about', views.AboutPage.as_view(), name='about'),
]
