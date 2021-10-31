from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_form, name='contact'),
    path('coaching_contact_form',
         views.coaching_contact_form, name='coaching_contact_form'),
    path('contact_manager/', views.contact_manager, name='contact_manager'),
    path('contact_detail/<int:contact_id>',
         views.contact_detail, name='contact_detail'),
    path('coaching_contact_detail/<int:contact_id>',
         views.coaching_contact_detail, name='coaching_contact_detail'),
]
