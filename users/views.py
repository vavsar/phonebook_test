from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from api.models import UserEditor
from .serializers import (UserSerializer, UserEditorSerializer, )

User = get_user_model()


class UserModelViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = AllowAny,

    def perform_create(self, serializer):
        if 'password' in self.request.data:
            password = make_password(self.request.data['password'])
            serializer.save(password=password)

    def perform_update(self, serializer):
        if 'password' in self.request.data:
            password = make_password(self.request.data['password'])
            serializer.save(password=password)
        else:
            serializer.save()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        current_user = get_object_or_404(User, id=self.request.user.id)
        if instance.id == current_user.id:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(
            {'Not allowed to delete other users'},
            status=status.HTTP_403_FORBIDDEN
        )


class UserEditorModelViewSet(viewsets.ModelViewSet):
    queryset = UserEditor.objects.all()
    serializer_class = UserEditorSerializer

    def perform_destroy(self, instance):
        if self.request.user == instance.user:
            instance.delete()
        return Response(
            {'Not allowed to delete other editor rights'},
            status=status.HTTP_403_FORBIDDEN
        )
