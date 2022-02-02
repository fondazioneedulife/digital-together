from unicodedata import category
from rest_framework import viewsets, generics
from .serializers import GymsSerializer, CoursesSerializer, CategorySerializer
from app.models import Gyms, Courses, Category
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view
class GymsViewSet(viewsets.ModelViewSet):
    """
    list of gyms or view a single gym
    """
    serializer_class = GymsSerializer
    queryset = Gyms.objects.all()
    #permission_classes = [IsAuthenticated]

class CoursesViewSet(viewsets.ModelViewSet):
    """
    list of Courses or view a single Course
    """
    serializer_class = CoursesSerializer
    queryset = Courses.objects.all()
    #permission_classes = [IsAuthenticated]


class CategoryViewSet(viewsets.ModelViewSet):
    """
    list of Category or view a single Course
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    #permission_classes = [IsAuthenticated]


@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')
    if query:
        queryset = Category.objects.filter(nome=query) 
        serializer = CategorySerializer(queryset, many=True)
        print(queryset)
        return Response(serializer.data)
    else:
        return Response({"category": []})
