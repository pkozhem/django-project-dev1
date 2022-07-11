from django.db import models


class Articles(models.Model):
    title = models.CharField('Title', max_length=100)
    preview = models.CharField('Preview', max_length=250)
    content = models.TextField('Article')
    date = models.DateTimeField('Publish date', auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'New'
        verbose_name_plural = 'News'
