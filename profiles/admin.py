from django.contrib import admin
from .models import UserProfile, Coach

class UserProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('user', 'full_name', 'email',
                       'phone_number')

    fields = ('user', 'full_name', 'email',
              'phone_number', 'is_coach')


class CoachAdmin(admin.ModelAdmin):

    fields = ('coach', 'about_me',
              'image_url', 'image')


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Coach, CoachAdmin)
