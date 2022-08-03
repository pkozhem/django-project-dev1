from django.contrib.auth import get_user_model
from django.db import models
from autoslug import AutoSlugField

User = get_user_model()


class Articles(models.Model):
    def instance(self):
        return self.title

    title = models.CharField('Title', max_length=100)
    preview = models.CharField('Preview', max_length=250)
    content = models.TextField('Article')
    date = models.DateTimeField('Publish date', auto_now_add=True)
    slug = AutoSlugField(populate_from=instance,
                         null=True, )
    amount_views = models.IntegerField('Amount_views', default=0, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.pk}'

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'


class Comment(models.Model):
    article = models.ForeignKey(Articles, on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField('Comment')
    date = models.DateTimeField('Publish date', auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.pk} PK comment details'

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
