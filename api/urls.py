from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import OrganisationModelViewSet, EmployeeModelViewSet


router_v1 = DefaultRouter()
router_v1.register('organisations', OrganisationModelViewSet, basename='organisations')
router_v1.register('employees', EmployeeModelViewSet, basename='employees')


urlpatterns = [
    path('v1/', include(router_v1.urls)),
]