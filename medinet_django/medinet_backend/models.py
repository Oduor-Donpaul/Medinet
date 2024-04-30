from django.db import models
from django.conf import settings
from django.utils.timezone import now

"""class AbstractUserModel(models.Model):
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(unique=True, null=True)
    dob = models.DateField(null=True)
    occupation = models.CharField(null=True, max_length=100)

    class Meta:
        abstract = True
"""

class AbstractTimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add =True)

    class Meta:
        abstract = True

class Practitioner (AbstractTimestampedModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    speciality = models.CharField(max_length=100)
    experience = models.IntegerField(default=0)
    start_availability = models.DateTimeField()
    end_availability = models.DateTimeField(default=now)
    image = models.ImageField()
    description = models.TextField()
    service = models.CharField(max_length=100)

    def __str__(self):
        return self.user.first_name

class Services(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    Practitioner = models.ForeignKey(Practitioner, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    

class Patient(AbstractTimestampedModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    medical_history = models.TextField()

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    practitioner = models.ForeignKey(Practitioner, on_delete=models.CASCADE)
    time = models.DateTimeField(null=True)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('confirmed', 'Confirmed')])

class Hospital(AbstractTimestampedModel):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    services = models.ManyToManyField(Services)
    rating = models.IntegerField()

class Disease(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    risk_score = models.IntegerField()

class HealthRiskAssessement(AbstractTimestampedModel):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    risk = models.ForeignKey(Disease, on_delete=models.CASCADE)

