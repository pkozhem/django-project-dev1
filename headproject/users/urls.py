from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register', views.Register.as_view(), name='register'),
    path('<slug>/', views.ProfileView.as_view(), name='profile'),
    path('<slug>/change_info', views.ProfileUpdateView.as_view(), name='change_info'),
]
