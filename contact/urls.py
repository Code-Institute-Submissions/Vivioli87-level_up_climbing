from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_form, name='contact'),
    path('contact_manager/', views.contact_manager, name='contact_manager'),
    path('contact_detail/<int:contact_id>', views.contact_detail, name='contact_detail'),
]