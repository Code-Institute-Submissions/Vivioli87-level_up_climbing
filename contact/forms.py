from django import forms
from .models import GeneralContact



class ContactForm(forms.ModelForm):
    class Meta:
        model = GeneralContact
        exclude = ('date_sent', 'is_complete')
    
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
        


class CompleteContactForm(forms.ModelForm):
    class Meta:
        model = GeneralContact
        fields = '__all__'

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
 
        self.fields['is_complete'] = forms.BooleanField(required=False, initial=False, label='Mark as complete?')
        for field in self.fields:
            if field != 'is_complete':
                self.fields[field].disabled = True
