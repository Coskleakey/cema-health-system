from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from clients.models import Client
from programs.models import Program
from .serializers import ClientSerializer, ProgramSerializer

class ClientListView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientDetailView(generics.RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ProgramListView(generics.ListAPIView):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
