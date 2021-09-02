from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Organisation, Employee

User = get_user_model()


class OrganisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisation
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

