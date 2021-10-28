from django.contrib import admin
from .models import Article

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):

    fields = ('title', 'content', 'image_url', 'image')

admin.site.register(Article, ArticleAdmin)
