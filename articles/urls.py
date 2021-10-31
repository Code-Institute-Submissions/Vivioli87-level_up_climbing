from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_articles, name='all_articles'),
    path('<int:article_id>/', views.article_detail, name='article_detail'),
    path('add/', views.add_article, name='add_article'),
    path('edit/<int:article_id>/', views.edit_article, name='edit_article'),
    path('delete/<int:article_id>/', views.delete_article,
         name='delete_article'),
    path('edit_comment/<int:comment_id>/', views.edit_comment,
         name='edit_comment'),
    path('delete_comment/<int:comment_id>/', views.delete_comment,
         name='delete_comment'),
]
