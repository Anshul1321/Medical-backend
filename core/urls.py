# core/urls.py
from django.urls import path
from .views import DoctorListCreate, AppointmentListCreate

urlpatterns = [
    path('doctors/', DoctorListCreate.as_view()),
    path('appointments/', AppointmentListCreate.as_view()),
]
