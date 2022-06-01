from django import forms
from django.contrib.auth.models import User
from .import models
from django.db import models

class EmployeeForm(forms.Form):
    full_name= forms.CharField(required=True)
    designation = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True)




