# from django.contrib import admin
# from myapp.models import Registration

# admin.site.register(Registration)

# myapp/admin.py
from django.contrib import admin
from .models import *

# Register the Registration model with the admin site
@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = (
        'full_name', 
        'registration_number', 
        'department', 
        'faculty', 
        'level', 
        'phone_number', 
        'gender'
    )
    search_fields = (
        'full_name', 
        'registration_number', 
        'department'
    )
