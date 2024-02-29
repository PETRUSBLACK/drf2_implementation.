from django.db import models
from user.models import CustomUser


STATUS_OPTIONS = (
    ("todo", "todo"),
    ("in_progress", "in_progress"),
    ("completed", "completed"),
)

class Task(models.Model):
    user = models.OneToOneField(CustomUser, related_name="user_task", on_delete=models.CASCADE)
    title = models.CharField(max_length=225)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    Status_options = models.CharField(
        max_length=100, choices=STATUS_OPTIONS, default="todo"
    )
    
