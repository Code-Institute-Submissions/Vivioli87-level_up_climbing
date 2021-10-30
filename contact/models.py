from django.db import models

from courses.models import Level
from venues.models import Venue


class GeneralContact(models.Model):
    full_name = models.CharField(max_length=80, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    message = models.TextField(null=False, blank=False)
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'General enquiry from {self.full_name}'


class PrivateCoachingContact(models.Model):
    full_name = models.CharField(max_length=80, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    level = models.ForeignKey(Level, on_delete=models.SET_NULL, 
                              blank=True, null=True)
    venue = models.ForeignKey(Venue, on_delete=models.SET_NULL,
                              blank=True, null=True)
    message = models.TextField(null=False, blank=False)
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Private Coaching enquiry from {self.full_name}'
