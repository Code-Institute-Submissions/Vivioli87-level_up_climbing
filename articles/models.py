from django.db import models

from profiles.models import UserProfile

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=254, null=False, blank=False)
    content = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ArticleComments(models.Model):
    article = models.ForeignKey(Article, null=False, blank=False,
                                on_delete=models.CASCADE)
    user_profile = models.ForeignKey(UserProfile, null=False, blank=False,
                                     on_delete=models.CASCADE)
    title = models.CharField(max_length=254, null=False, blank=False)
    comment = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
         verbose_name_plural = "Article Comments"

    def __str__(self):
        return self.title

