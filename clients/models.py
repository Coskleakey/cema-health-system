from django.db import models
from programs.models import Program


# Create your models here.
class Client(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    full_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    contact_info = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name
    
class Enrollment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='enrollments')
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    date_enrolled = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.client.full_name} - {self.program.name}"