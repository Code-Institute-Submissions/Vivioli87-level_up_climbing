from django.shortcuts import render

from .models import Article


def all_articles(request):

    articles = Article.objects.all()

    template = 'articles/all_articles.html'
    context = {
        'articles': articles,
    }

    return render(request, template, context)
