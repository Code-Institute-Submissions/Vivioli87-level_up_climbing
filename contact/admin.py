from django.contrib import admin
from .models import GeneralContact, PrivateCoachingContact


class GeneralContactAdmin(admin.ModelAdmin):

    fields = ('full_name', 'email', 'phone_number', 'message', 'is_complete')


class PrivateCoachingContactAdmin(admin.ModelAdmin):

    fields = ('full_name', 'email', 'phone_number',
              'message', 'level', 'venue', 'is_complete')


admin.site.register(GeneralContact, GeneralContactAdmin)
admin.site.register(PrivateCoachingContact, PrivateCoachingContactAdmin)
