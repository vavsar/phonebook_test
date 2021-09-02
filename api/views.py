from rest_framework import viewsets

from .models import Organisation, Employee
from .serializers import OrganisationSerializer, EmployeeSerializer


class OrganisationModelViewSet(viewsets.ModelViewSet):
    queryset = Organisation.objects.all()
    serializer_class = OrganisationSerializer
    # permission_classes = (IsAdminOrReadOnly,)
    # pagination_class = PageNumberPagination
    # filter_backends = [DjangoFilterBackend]
    # filterset_class = TitleFilter
    # filterset_fields = ['slug', ]


class EmployeeModelViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
