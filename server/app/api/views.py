from rest_framework import viewsets, generics
from .serializers import GymsSerializer, CoursesSerializer, CategorySerializer
from app.models import Gyms, Courses, Category


class GymsViewSet(viewsets.ModelViewSet):
    """
    list of gyms or view a single gym
    """
    serializer_class = GymsSerializer
    queryset = Gyms.objects.all()

class CoursesViewSet(viewsets.ModelViewSet):
    """
    list of Courses or view a single Course
    """
    serializer_class = CoursesSerializer
    queryset = Courses.objects.all()

class CategoryViewSet(viewsets.ModelViewSet):
    """
    list of Category or view a single Course
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()