from django import forms
from django.forms.widgets import ClearableFileInput

from .models import Article, ArticleComments


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ('created_date',)

    image = forms.ImageField(label='Image', required=False, widget=ClearableFileInput)

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Title',
            'content': 'Content',
            'image_url': 'Image URL',
            'image': 'Image',
        }

        self.fields['title'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0'
            self.fields[field].label = False


class ArticleCommentForm(forms.ModelForm):

    class Meta:
        model = ArticleComments
        exclude = ('created_date',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'article': 'Article',
            'user_profile': 'Username',
            'title': 'Title',
            'comment': 'Comment',
        }

        self.fields['title'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0'
            self.fields[field].label = False
            self.fields['article'].disabled = True
            self.fields['user_profile'].disabled = True
