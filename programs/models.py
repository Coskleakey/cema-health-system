from django.db import models

class Program(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField(default='2025-01-01')
    end_date = models.DateField(default='2026-01-01')

    def __str__(self):
        return self.name
