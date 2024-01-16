from django.contrib import admin

# Register your models here.
from .models import Blog, Car

admin.site.register((Blog, Car))