from django import forms

from .models import ArticleComments


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
