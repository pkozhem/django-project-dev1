from django.urls import reverse
from django.views.generic import DetailView, TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import render, redirect
from django.db.models import F
from .models import Articles
from .forms import ArticlesForm


class NewsHomeView(TemplateView):
    template_name = 'newsapp/news.html'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['news_data'] = Articles.objects.order_by('-date')
        return contex


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'newsapp/news_detail.html'
    context_object_name = 'news_data'

    def get_object(self, queryset=None):
        slug = self.kwargs.get(self.slug_url_kwarg)
        data = Articles.objects.get(slug=slug)
        data.amount_views = F('amount_views') + 1
        data.save()
        return data


class NewsUpdateView(LoginRequiredMixin, UpdateView):
    model = Articles
    template_name = 'newsapp/update.html'
    context_object_name = 'news_data'
    form_class = ArticlesForm

    def get_success_url(self):
        view_name = 'news-detail'
        return reverse(view_name, kwargs={'slug': self.object.slug})


class NewsCreate(LoginRequiredMixin, TemplateView):
    model = Articles
    template_name = 'newsapp/create.html'

    def post(self, request):
        form = ArticlesForm(request.POST) or None
        if form.is_valid():
            article = form.save(commit=False)
            if request.user.is_authenticated:
                article.author = request.user
            else:
                article.author = None
            article.save()
            return redirect('news')
        messages.error(request, f'Invalid credentials. Try again')
        context = self.get_context_data(form=form)
        return context

    def get(self, request, *args, **kwargs):
        context = {
            'form': ArticlesForm()
        }
        return render(request, self.template_name, context)


def news_delete(request, slug):
    article = Articles.objects.get(slug=slug)
    article.delete()
    return redirect('news')
