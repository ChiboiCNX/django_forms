# models.py
from django.db import models

class Registration(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Not sure', 'Not sure'),
        ('Queer', 'Queer'),
        ('Prefer not to say', 'Prefer not to say'),
    ]

    full_name = models.CharField(max_length=255)
    registration_number = models.CharField(max_length=20)
    department = models.CharField(max_length=100)
    faculty = models.CharField(max_length=100)
    level = models.IntegerField()
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)

    def __str__(self):
        return self.full_name
