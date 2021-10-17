import uuid

from django.db import models

from courses.models import Course


class Booking(models.Model):

    booking_reference = models.CharField(max_length=32, null=False,
                                         editable=False)
    full_name = models.CharField(max_length=60, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    booking_total = models.DecimalField(max_digits=10, decimal_places=2,
                                        null=False, blank=False)
    booked_course = models.CharField(max_length=60, null=False, blank=False)

    def _create_booking_reference(self):
        """
        Generate a random, unique booking reference using UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the booking refernce
        if it hasn't been set already.
        """
        if not self.booking_reference:
            self.booking_reference = self._create_booking_reference()
        
        super().save(*args, **kwargs)

    def __str__(self):
        return self.booking_reference
