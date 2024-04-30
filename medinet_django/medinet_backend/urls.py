from . import views
from django.urls import path, include

urlpatterns = [
        path('practitioner/', views.practitioner_view, name='practitioner-list'),
        path('practitioner/<int:pk>/', views.practitioner_detail_view, name='practitioner-detail'),
        path('disease/<int:pk>/', views.disease_view, name='disease-detail'),
        path('patient/<int:pk>/', views.patient_view, name='patient-detail'),
        path('appointment/<int:pk>/', views.appointment_view, name='appointment-detail'),
        path('hospital/', views.hospital_view, name='hospital-list'),
        path('hospital/<int:pk>/',  views.hospital_detail_view, name='hospital-detail'),
        path('risk/<int:pk>/', views.risk_assessement_view, name='risk-detail'),
        path('services/',views.services_view, name='services-list'),
        path('service/<int:pk>/', views.service_detail_view, name='service-datails'),
        path('register/', views.register_view, name='register'),
        path('login/', views.login, name='login'),

        ]
