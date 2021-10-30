from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Article, ArticleComments
from profiles.models import UserProfile
from .forms import ArticleForm, ArticleCommentForm


def all_articles(request):

    articles = Article.objects.all().order_by('-created_date')

    page = request.GET.get('page', 1)
    paginator = Paginator(articles, 6)

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)



    template = 'articles/all_articles.html'
    context = {
        'articles': articles,
    }

    return render(request, template, context)


def article_detail(request, article_id):

    article = get_object_or_404(Article, pk=article_id)
    comments = ArticleComments.objects.filter(article=article).order_by('-created_date')
    profile = get_object_or_404(UserProfile, user=request.user)

    page = request.GET.get('page', 1)
    paginator = Paginator(comments, 4)

    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        comments = paginator.page(1)
    except EmptyPage:
        comments = paginator.page(paginator.num_pages)

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
        'profile': profile,
    }

    return render(request, template, context)

@login_required
def add_article(request):
    """ Add an article """
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
    """ Edit an article """
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


@login_required
def delete_article(request, article_id):
    """" Delete an article """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only the website owner can do that.')
        return redirect(reverse('home'))

    article = get_object_or_404(Article, pk=article_id)
    article.delete()
    messages.success(request, 'Article deleted!')
    return redirect(reverse('all_articles'))


@login_required
def edit_comment(request, comment_id):
    """ Edit a comment """

    comment = get_object_or_404(ArticleComments, pk=comment_id)
    profile = get_object_or_404(UserProfile, user=request.user)
    article = comment.article

    if profile != comment.user_profile:
        messages.error(request, 'Sorry, you do not have permissions to edit this comment.')
        return redirect(reverse('all_articles'))

    if request.method == 'POST':
        form = ArticleCommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated article!')
            return redirect(reverse('article_detail', args=[article.id]))
        else:
            messages.error(request,
                           ('Failed to edit comment.'
                            'Please ensure the form is valid.'))
    else:
        form = ArticleCommentForm(instance=comment)

    template = 'articles/edit_comment.html'
    context = {
        'form': form,
        'comment': comment
    }

    return render(request, template, context)


@login_required
def delete_comment(request, comment_id):
    """" Delete comment """
    comment = get_object_or_404(ArticleComments, pk=comment_id)
    profile = get_object_or_404(UserProfile, user=request.user)
    article = comment.article

    if profile != comment.user_profile:
        messages.error(request, 'Sorry, you do not have permissions to delete this comment.')
        return redirect(reverse('article_detail', args=[article.id]))

    comment.delete()
    messages.success(request, 'Comment deleted!')
    return redirect(reverse('article_detail', args=[article.id]))
