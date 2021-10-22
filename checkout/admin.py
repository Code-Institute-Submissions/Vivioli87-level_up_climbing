from django.contrib import admin
from .models import Booking


class BookingAdmin(admin.ModelAdmin):
    readonly_fields = ('user_profile', 'booking_reference', 'date',
                       'booking_total', 'booked_course',)

    fields = ('user_profile', 'booking_reference', 'booked_course', 'date',
              'full_name', 'email', 'phone_number',
              'booking_total',)

    list_display = ('booking_reference', 'booked_course', 'date',
                    'user_profile', 'full_name', 'email',
                    'phone_number',)

    ordering = ('-date',)


admin.site.register(Booking, BookingAdmin)
