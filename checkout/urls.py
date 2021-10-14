from django.urls import path
from . import views

urlpatterns = [
    path('<int:course_id>/', views.booking, name='booking'),
]
