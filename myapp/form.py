# forms.py
from django import forms
from .models import Registration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['full_name', 'registration_number', 'department', 'faculty', 'level', 'phone_number', 'gender']
        widgets = {
            'gender': forms.RadioSelect(choices=Registration.GENDER_CHOICES),
        }
