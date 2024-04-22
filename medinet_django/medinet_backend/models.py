from django.db import models
from django.conf import settings

class AbstractUserModel(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.EmailField(unique=True)
    dob = models.DateField()
    occupation = models.CharField(max_length=100)

    class Meta:
        abstract = True


class AbstractTimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add =True)

    class Meta:
        abstract = True

class Practitioner(AbstractTimestampedModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    speciality = models.CharField(max_length=100)
    years_of_experience = models.IntegerField()

class Patient(AbstractTimestampedModel, AbstractUserModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    medical_history = models.TextField()

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    practitioner = models.ForeignKey(Practitioner, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('confirmed', 'Confirmed')])

class Hospital(AbstractTimestampedModel):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.IntegerField()

class Disease(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    risk_score = models.IntegerField()

class HealthRiskAssessement(AbstractTimestampedModel):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    risk = models.ForeignKey(Disease, on_delete=models.CASCADE)

