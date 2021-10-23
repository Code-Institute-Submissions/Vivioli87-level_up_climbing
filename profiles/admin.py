from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('user', 'full_name', 'email',
                       'phone_number')

    fields = ('user', 'full_name', 'email',
              'phone_number', 'is_coach')


admin.site.register(UserProfile, UserProfileAdmin)
