from rest_framework import generics, filters
from .models import Doctor, Appointment
from .Serializers import DoctorSerializer, AppointmentSerializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

class DoctorListCreate(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

@method_decorator(csrf_exempt, name='dispatch')
class AppointmentListCreate(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['doctor__id', 'date']
