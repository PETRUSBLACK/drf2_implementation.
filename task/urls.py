from django.urls import path, include
from .views import TaskRetrieveAPIView, TaskList, TaskUpdateDestroyView

urlpatterns = [
    path('list_create', TaskList.as_view()),    
    path('retrieve/pk', TaskRetrieveAPIView.as_view()),
    path('update+delete/pk', TaskUpdateDestroyView.as_view()),
]
