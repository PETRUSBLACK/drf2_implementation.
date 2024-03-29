from django.contrib import admin
from django.urls import path, include
from django.conf import settings 

from rest_framework.routers import DefaultRouter

router = DefaultRouter()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include("auth_user.urls")),
    path('task/', include("task.urls"))

]

if settings.DEBUG:
    import debug_toolbar
    
    urlpatterns = [
        path('__debut__/', include(debug_toolbar.urls))
    ] + urlpatterns 
