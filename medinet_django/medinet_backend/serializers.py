from .models import Practitioner, Patient, Appointment, Hospital, Disease, HealthRiskAssessement
from rest_framework import serializers

class PractitionerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Practitioner
        fields = '__all__'


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'

class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease
        fields = '__all__'

class HealthRiskAssessementSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthRiskAssessement
        fields = '__all__'
