from rest_framework import serializers
from clients.models import Client, Enrollment
from programs.models import Program

class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = ['id', 'name', 'description']

class EnrollmentSerializer(serializers.ModelSerializer):
    program = ProgramSerializer()

    class Meta:
        model = Enrollment
        fields = ['id', 'program', 'date_enrolled']

class ClientSerializer(serializers.ModelSerializer):
    enrollments = EnrollmentSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        fields = ['id', 'full_name', 'age', 'gender', 'contact_info', 'enrollments']
