from django.contrib import admin

from .models import Venue


class VenueAdmin(admin.ModelAdmin):
    readonly_fields = ('name', 'street_address1',
                       'street_address2', 'town_or_city',
                       'postcode', 'lat', 'lng')

    fields = ('name', 'street_address1',
                      'street_address2', 'town_or_city',
                      'postcode', 'lat', 'lng', 'map_marker')

    list_display = ('name', 'postcode')


admin.site.register(Venue, VenueAdmin)
