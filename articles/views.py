from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Article, ArticleComments
from profiles.models import UserProfile
from .forms import ArticleCommentForm


def all_articles(request):

    articles = Article.objects.all()

    template = 'articles/all_articles.html'
    context = {
        'articles': articles,
    }

    return render(request, template, context)


def article_detail(request, article_id):

    article = get_object_or_404(Article, pk=article_id)
    comments = ArticleComments.objects.filter(article=article).order_by('-created_date')
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = ArticleCommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added article comment!')
            return redirect(reverse('article_detail', args=[article.id]))
        else:
            messages.error(request,
                           ('Failed to add article comment. '
                            'Please ensure the form is valid.'))
    else:
        form = ArticleCommentForm(initial={
            'article': article,
            'user_profile': profile
        })

    template = 'articles/article_detail.html'
    context = {
        'form': form,
        'article': article,
        'comments': comments,
    }

    return render(request, template, context)
