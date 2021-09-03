from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import (OrganisationModelViewSet, FirmEmployeeModelViewSet,
                    OwnEmployeeModelViewSet)

router_v1 = DefaultRouter()
router_v1.register('organisations',
                   OrganisationModelViewSet,
                   basename='organisations')
router_v1.register(r'organisations/(?P<organisation_id>\d+)/employees',
                   FirmEmployeeModelViewSet,
                   basename='firm_employees'
                   )
router_v1.register('employees',
                   OwnEmployeeModelViewSet,
                   basename='own_employees'
                   )

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
