from django.urls import path
from . import views


urlpatterns = [
    path('', views.NewsHomeView.as_view(), name='news'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name='news-update'),
    path('delete/<int:id>', views.news_delete),
]
