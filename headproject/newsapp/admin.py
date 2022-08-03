from django.contrib import admin
from .models import Articles, Comment


class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date', 'slug')
    search_fields = ('title', 'author', 'date')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'article', 'author', 'date')
    search_fields = ('pk', 'article', 'author', 'date')


admin.site.register(Articles, ArticlesAdmin)
admin.site.register(Comment, CommentAdmin)
