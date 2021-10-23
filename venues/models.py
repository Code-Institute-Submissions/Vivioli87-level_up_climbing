from django.db import models


class Venue(models.Model):
    name = models.CharField(max_length=254, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=False, blank=False)
    lat = models.DecimalField(max_digits=10, decimal_places=6)
    lng = models.DecimalField(max_digits=10, decimal_places=6)
    map_marker = models.CharField(max_length=1, null=False, blank=False)

    def __str__(self):
        return self.name