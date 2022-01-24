from django.contrib import admin
from .models import Courses, Gyms

arr = [Gyms, Courses] 

admin.site.register(arr)