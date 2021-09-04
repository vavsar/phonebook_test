from django.contrib.auth import get_user_model
from rest_framework import viewsets, status, filters, mixins
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import Organisation, Employee
from .serializers import (OrganisationSerializer, FirmEmployeeSerializer,
                          OwnEmployeeSerializer, )

User = get_user_model()


class OrganisationModelViewSet(viewsets.ModelViewSet):
    serializer_class = OrganisationSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('title',
                     'employees__last_name',
                     'employees__first_name',
                     'employees__middle_name',
                     'employees__private_phone',
                     'employees__work_phone',
                     )
    ordering = ('title',)

    def get_queryset(self):
        queryset = Organisation.objects.all()
        # queryset = Organisation.objects.filter(owner=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        if instance.owner == request.user:
            serializer = self.get_serializer(instance, data=request.data,
                                             partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            if getattr(instance, '_prefetched_objects_cache', None):
                instance._prefetched_objects_cache = {}

            return Response(serializer.data)
        return Response(
            {'You can update only own organisations'},
            status=status.HTTP_403_FORBIDDEN
        )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.owner.id == self.request.user.id:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(
            {'You can delete only own organisations'},
            status=status.HTTP_403_FORBIDDEN
        )


class FirmEmployeeModelViewSet(viewsets.ModelViewSet):
    serializer_class = FirmEmployeeSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = (
        'first_name',
        'last_name',
        'private_phone',
        'work_phone'
    )

    def get_queryset(self):
        organisation = get_object_or_404(Organisation,
                                         pk=self.kwargs.get('organisation_id'))
        # return organisation.employees.filter(creator=self.request.user)
        return organisation.employees.all()

    def perform_create(self, serializer):
        organisation = get_object_or_404(Organisation,
                                         pk=self.kwargs.get('organisation_id'))
        serializer.save(organisation=organisation, creator=self.request.user)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        if instance.creator.id == self.request.user.id:
            serializer = self.get_serializer(instance, data=request.data,
                                             partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            if getattr(instance, '_prefetched_objects_cache', None):
                instance._prefetched_objects_cache = {}

            return Response(serializer.data)
        return Response(
            {'You can update only own employees'},
            status=status.HTTP_403_FORBIDDEN
        )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.creator.id == self.request.user.id:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(
            {'You can delete only own organisations'},
            status=status.HTTP_403_FORBIDDEN
        )


class OwnEmployeeModelViewSet(mixins.ListModelMixin,
                              GenericViewSet):
    serializer_class = OwnEmployeeSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = (
        'first_name',
        'last_name',
        'private_phone',
        'work_phone'
    )

    def get_queryset(self):
        return Employee.objects.filter(creator=self.request.user)
