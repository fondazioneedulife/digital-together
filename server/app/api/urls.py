from django.urls import path
from django.urls.conf import include, path
from rest_framework import routers

from .views import GymsViewSet, CoursesViewSet

router = routers.DefaultRouter()
router.register(r'palestre', GymsViewSet,  basename='palestre')
router.register(r'corsi', CoursesViewSet,  basename='corsi')

urlpatterns = [
    path("", include(router.urls)),
]