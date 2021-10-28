from django.shortcuts import render, get_object_or_404

from .models import Article


def all_articles(request):

    articles = Article.objects.all()

    template = 'articles/all_articles.html'
    context = {
        'articles': articles,
    }

    return render(request, template, context)


def article_detail(request, article_id):

    article = get_object_or_404(Article, pk=article_id)

    template = 'articles/article_detail.html'
    context = {
        'article': article,
    }

    return render(request, template, context)
