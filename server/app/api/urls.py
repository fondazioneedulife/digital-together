from django.urls import path
from django.urls.conf import include, path
from rest_framework import routers
from app.api import views

from .views import GymsViewSet, CoursesViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register(r'palestre', GymsViewSet,  basename='palestre')
router.register(r'corsi', CoursesViewSet,  basename='corsi')
router.register(r'categorie', CategoryViewSet,  basename='categorie')

urlpatterns = [
    path("corsi/search/", views.search),
    path("", include(router.urls)),
]