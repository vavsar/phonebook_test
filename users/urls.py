from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UserModelViewSet, UserEditorModelViewSet

router_v1 = DefaultRouter()
router_v1.register('users', UserModelViewSet, basename='users')
router_v1.register('editors', UserEditorModelViewSet, basename='editors')


urlpatterns = [
    path('v1/', include(router_v1.urls)),
]