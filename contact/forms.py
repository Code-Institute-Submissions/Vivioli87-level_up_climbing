from django import forms
from .models import GeneralContact, PrivateCoachingContact

from venues.models import Venue
from courses.models import Level


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

        self.fields['is_complete'] = forms.BooleanField(required=False,
                                                        initial=False,
                                                        label='Mark as complete?')
        for field in self.fields:
            if field != 'is_complete':
                self.fields[field].disabled = True


class PrivateCoachingForm(forms.ModelForm):
    class Meta:
        model = PrivateCoachingContact
        exclude = ('date_sent', 'is_complete')

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email',
            'phone_number': 'Phone number',
            'message': 'Message',
            'level': 'Level',
            'venue': 'Venue',
        }

        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0'
            self.fields['level'] = forms.ModelChoiceField(queryset=Level.objects.all(),
                                                          label='Current Level')
            self.fields['venue'] = forms.ModelChoiceField(queryset=Venue.objects.all(),
                                                          label='Preferred Venue')
            self.fields[field].label = False


class CompletePrivateCoachingForm(forms.ModelForm):
    class Meta:
        model = PrivateCoachingContact
        fields = '__all__'

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.fields['is_complete'] = forms.BooleanField(required=False,
                                                        initial=False,
                                                        label='Mark as complete?')
        for field in self.fields:
            if field != 'is_complete':
                self.fields[field].disabled = True
