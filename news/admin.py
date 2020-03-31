
from django.contrib import admin 

from news.models import News, Category, Tag, Comments

admin.site.register(News)
admin.site.register(Category)
admin.site.register(Tag)

@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    """Комментарии"""
    list_display = ('user', 'new', 'created', 'moderation')

