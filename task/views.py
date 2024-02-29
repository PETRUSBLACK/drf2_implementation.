from django.shortcuts import render
from rest_framework import filters, status, viewsets, serializers, generics
from .models import Task
from rest_framework.pagination import PageNumberPagination
from .serializer import TaskSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.decorators import action
from django.core.cache import cache


class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAdminUser]    
    pagination_class = PageNumberPagination

class TaskUpdateDestroyView(generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAdminUser]
    
class TaskRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated] 
    
    @action(
        methods=["POST"],
        detail=False,
        serializer_class=TaskSerializer,
        permission_classes=[IsAdminUser],
        url_path="Updating_a_task",
    )
    def updating_task(self, request, pk=None):
        """This endpoint invites new user"""
        task = self.get_object()
        if task:
            task.completed = True
            task.Status_options = completed
            task.save()
            return Response(
                {"success": True, "data": serializer.data}, status=status.HTTP_200_OK
            )
        return Response(
            {"success": False, "errors": serializer.errors}, status.HTTP_400_BAD_REQUEST
        )
        
    @action(
        methods=["POST"],
        detail=True,
        serializer_class=None,
        url_path="Analytics_Dashboard:",
        permission_classes=[IsAdminUser],
    )
    def activate_group_admin(self, request, pk=None):
        qs = self.queryset
        response_data = {
            "success": True,
            "Total number of tasks": qs,
            "Number of Todo tasks": qs.filter(Status_options="todo"),
            "Number of in_progress tasks": qs.filter(Status_options="in_progress"),
            "Number of completed tasks": qs.filter(Status_options="completed"),
        }
        return Response(response_data, status=status.HTTP_200_OK)
    
    
# class TaskDestroyAPIView(generics.DestroyAPIView):
#     queryset = Task.objects.all()
#     permission_classes = [IsAdminUser]
    