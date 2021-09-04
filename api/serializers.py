from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Organisation, Employee, UserEditor

User = get_user_model()


class OrganisationSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Organisation
        fields = ('id', 'title', 'owner', 'address', 'description')

    def to_representation(self, instance):
        output_data = super().to_representation(instance)
        employees = instance.employees.all()[:5]
        list_employees = [FirmEmployeeSerializer(person).data for person in employees]
        output_data['employee'] = list_employees
        return output_data

    def create(self, validated_data):
        request = self.context['request']
        instance = Organisation.objects.create(**validated_data)
        UserEditor.objects.create(
            user=request.user,
            organisation=instance
        )
        return instance


class FirmEmployeeSerializer(serializers.ModelSerializer):
    creator = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Employee
        fields = '__all__'

    def create(self, validated_data):
        if 'private_phone' not in validated_data and 'work_phone' not in validated_data:
            raise serializers.ValidationError(
                'At least one phone number must be filled!')
        instance = Employee.objects.create(**validated_data)
        return instance


class OwnEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

