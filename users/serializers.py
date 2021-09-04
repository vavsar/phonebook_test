from django.contrib.auth import get_user_model
from rest_framework import serializers
from api.models import UserEditor

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class UserEditorSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserEditor
        fields = ('id', 'user', 'organisation')

    def create(self, validated_data):
        request = self.context['request']
        user = request.user
        if UserEditor.objects.filter(
                user=user,
                organisation=validated_data['organisation']).exists():
            instance = UserEditor.objects.create(**validated_data)
            return instance
        raise serializers.ValidationError(
                'You have to be the creator of this organisation')
