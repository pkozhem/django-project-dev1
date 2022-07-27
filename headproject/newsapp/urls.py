from django.urls import path
from . import views


urlpatterns = [
    path('', views.AllArticles.as_view(), name='news'),
    path('create', views.CreateArticle.as_view(), name='create'),
    path('<slug>', views.ReadArticle.as_view(), name='news-detail'),
    path('<slug>/update', views.UpdateArticle.as_view(), name='news-update'),
    path('delete/<slug>', views.DeleteArticle.as_view()),
]
