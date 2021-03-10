from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content', 'created_at', 'updated_at',)

# Register your models here.
admin.site.register(Article, ArticleAdmin)

# admin site에 register하겠다.
