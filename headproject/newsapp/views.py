from django.contrib.auth import get_user_model
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import render, redirect
from django.db.models import F
from .models import Articles, Comment
from .forms import ArticlesForm, CommentForm

User = get_user_model()


class AllArticles(TemplateView):
    template_name = 'newsapp/news.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_data'] = Articles.objects.order_by('-date')
        return context


class ReadArticle(View):
    template_name = 'newsapp/news_detail.html'

    def get(self, request, slug):
        article = Articles.objects.get(slug=slug)
        comment = Comment.objects.filter(article_id=article.id).all()
        context = {
            'news_data': article,
            'comment': comment,
            'form': CommentForm(),
        }
        article.amount_views = F('amount_views') + 1
        article.save()
        return render(request, self.template_name, context)

    def post(self, request, slug):
        form = CommentForm(request.POST) or None
        if form.is_valid():
            comment = form.save(commit=False)
            if request.user.is_authenticated:
                comment.author = request.user
                article = Articles.objects.get(slug=slug)
                comment.article_id = article.id
            else:
                comment.author = None
            comment.save()
            return redirect('news-detail', slug=slug)
        messages.error(request, f'Invalid credentials. Try again')
        return redirect('news-detail', slug=slug)


class UpdateArticle(LoginRequiredMixin, UpdateView):
    model = Articles
    template_name = 'newsapp/update.html'
    context_object_name = 'news_data'
    form_class = ArticlesForm

    def get_success_url(self):
        view_name = 'news-detail'
        return reverse(view_name, kwargs={'slug': self.object.slug})


class DeleteArticle(LoginRequiredMixin, View):
    @staticmethod
    def get(request, slug):
        article = Articles.objects.get(slug=slug)
        article.delete()
        return redirect('news')


class CreateArticle(LoginRequiredMixin, TemplateView):
    model = Articles
    template_name = 'newsapp/create.html'

    def get(self, request, *args, **kwargs):
        context = {
            'form': ArticlesForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = ArticlesForm(request.POST) or None
        if form.is_valid():
            article = form.save(commit=False)
            exist_titles = Articles.objects.only('title')
            for title in exist_titles:
                if article.title == str(title):
                    messages.error(request, f'This title is already exists')
                    context = self.get_context_data(form=form)
                    del article, form
                    return render(request, self.template_name, context)
            if request.user.is_authenticated:
                article.author = request.user
            else:
                article.author = None
            article.save()
            return redirect('news')
        messages.error(request, f'Invalid credentials. Try again')
        context = self.get_context_data(form=form)
        return context
