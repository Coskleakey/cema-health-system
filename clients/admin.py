from django.contrib import admin
from .models import Client, Enrollment

# Register your models here.
admin.site.register(Client)
admin.site.register(Enrollment)