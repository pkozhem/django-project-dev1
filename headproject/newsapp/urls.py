from django.urls import path
from . import views


urlpatterns = [
    path('', views.NewsHomeView.as_view(), name='news'),
    path('create', views.NewsCreate.as_view(), name='create'),
    path('<slug>', views.NewsDetailView.as_view(), name='news-detail'),
    path('<slug>/update', views.NewsUpdateView.as_view(), name='news-update'),
    path('delete/<slug>', views.NewsDelete.as_view()),
]
