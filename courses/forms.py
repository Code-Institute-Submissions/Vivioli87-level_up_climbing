from django import forms


from .models import Course, CourseType
from venues.models import Venue
from profiles.models import Coach

class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['venue'] = forms.ModelChoiceField(queryset=Venue.objects.all())
        self.fields['coach'] = forms.ModelChoiceField(queryset=Coach.objects.all())
        self.fields['course_complete'] = forms.BooleanField(required=False, initial=False, label='Course finished?')
        self.fields['start_date'] = forms.DateTimeField()
