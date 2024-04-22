from django.contrib import admin
from django.apps import apps
from django.contrib.auth.models import Group, User
# Register your models here.

models = apps.get_models()

for model in models:
    if model != Group and model != User:
        admin.site.register(model)
