from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=254, null=False, blank=False)
    content = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title