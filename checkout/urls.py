from django.urls import path
from . import views
from .webhooks import webhook


urlpatterns = [
    path('<int:course_id>/', views.booking, name='booking'),
    path('booking_success/<booking_reference>/', views.booking_success,
         name='booking_success'),
    path('wh/', webhook, name='webhook'),
]
