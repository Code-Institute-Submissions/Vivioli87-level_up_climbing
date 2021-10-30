from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_form, name='contact'),
    path('contact_manager/', views.contact_manager, name='contact_manager')
]