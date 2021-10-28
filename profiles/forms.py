from django import forms
from .models import UserProfile, Coach


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user', 'is_coach',)
    
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email',
            'phone_number': 'Phone Number',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'
            self.fields[field].label = False


# class CoachForm(forms.ModelForm):
#     class Meta:
#         model = Coach
#         exclude = ('coach',)
    

#     def __init__(self, *args, **kwargs):

#         super().__init__(*args, **kwargs)
#         placeholders = {
#             'about_me': 'About Me',
#             'default_email': 'Email',
#             'default_phone_number': 'Phone Number',
#         }

#          self.fields['default_full_name'].widget.attrs['autofocus'] = True
#          for field in self.fields:
#             placeholder = placeholders[field]
#             self.fields[field].widget.attrs['placeholder'] = placeholder
#             self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'
#             self.fields[field].label = False