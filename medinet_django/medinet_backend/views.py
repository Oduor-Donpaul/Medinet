from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework import status

# Create your views here.

@api_view(['GET', 'POST'])
def practitioner_view(request):
    if request.method == 'POST':
        serializer_data = PractitionerSerializer(data = request.data)
       
        if serializer_data.is_valid():
            instance = serializer_data.save()
            return Response(serializer_data.data, status=status.HTTP_201_CREATED)
       
        return Response(serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        queryset = Practitioner.objects.all()
        serializer_data = PractitionerSerializer(queryset, many=True)
        return Response(serializer_data.data)

@api_view(['GET', 'PUT', 'DELETE'])
def practitioner_detail_view(request, pk):
    try:
        practitioner = Practitioner.objects.get(pk=pk)
    except Practitioner.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PractitionerSerializer(practitioner)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PractitionerSerializer(practitioner, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method =='DELETE':
        practitioner.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def patient_view(request, pk):
    try:
        patient = Patient.objects.get(pk=pk)
    except patient.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = PatientSerializer(patient)
        return Response(serializer.data)

    elif request.mathod == 'PUT':
        serializer = PatientSerializer(patient, data=request.data)

        if serializer.s_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUESST)

    elif request.method == 'POST':
        serializer = PatientSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'PUT'])
def appointment_view(request, pk):
    try:
        appointment = Appointment.objects.get(pk=pk)
    except appointment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AppointmentSerializer(appointment)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AppointmentSrializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        serializer = AppointmentSerializer(appointment, data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def hospital_view(request):
    if request.method == 'GET':
        queryset = Hospital.objects.all()
        serializer = HospitalSerializer(queryset, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = HospitalSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def hospital_detail_view(request, pk):
    try:
        hospital = Hospital.objects.get(pk=pk)
    except Hospital.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = HospitalSerializer(hospital)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = HospitalSerializer(hospital, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        hospita.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def risk_assessement_view(request, pk):
    try:
        risk = HealthRiskAssessement.objects.get(pk=pk)
    except risk.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = HealthRiskAssessemetSerializer(risk)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = HealthRiskAssessement(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status_HTTP_201_CREATED)


@api_view(['GET'])
def disease_view(request, pk):
    try:
        disease = Disease.objects.get(pk=pk)
    except Disease.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DiseaseSerializer(disease)
        return Response(serializer.data)

 
