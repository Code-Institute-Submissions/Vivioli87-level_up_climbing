from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Article, ArticleComments
from profiles.models import UserProfile
from .forms import ArticleForm, ArticleCommentForm


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
        form = ArticleCommentForm(request.POST, initial={'article': article,
                                                         'user_profile': profile})
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

@login_required
def add_article(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you do not have permissions to do that.')
        return redirect(reverse('home'))
    
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
            messages.success(request, 'Successfully added article!')
            return redirect(reverse('article_detail', args=[article.id]))
        else:
            messages.error(request,
                           ('Failed to add course. '
                            'Please ensure the form is valid.'))
    else:
        form = ArticleForm()

    template = 'articles/add_article.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_article(request, article_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you do not have permissions to do that.')
        return redirect(reverse('home'))

    article = get_object_or_404(Article, pk=article_id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated article!')
            return redirect(reverse('article_detail', args=[article.id]))
        else:
            messages.error(request,
                           ('Failed to edit course.'
                            'Please ensure the form is valid.'))
    else:
        form = ArticleForm(instance=article)

    template = 'articles/edit_article.html'
    context = {
        'form': form,
        'article': article
    }

    return render(request, template, context)
