from django import forms
from .models import GeneralContact


class ContactForm(forms.ModelForm):
    class Meta:
        model = GeneralContact
        exclude = ('date_sent',)
    
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email',
            'phone_number': 'Phone number',
            'message': 'Message',
        }

        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0'
            self.fields[field].label = False
