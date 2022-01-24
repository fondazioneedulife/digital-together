from django.contrib import admin
from .models import Courses, Gyms, Category

arr = [Gyms, Courses, Category] 

admin.site.register(arr)