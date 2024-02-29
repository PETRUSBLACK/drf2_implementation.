from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.cache import cache
from .models import Task

@receiver(post_save, sender=Task)
def update_task_cache(sender, instance, **kwargs):
    
    # Update the cached list of tasks
    cached_tasks = cache.get('tasks_list')
    if cached_tasks is not None:
        
        # Update the cached list of tasks
        if instance.completed:
            
            # If the task is marked as completed, remove it from the list
            cached_tasks.remove(instance.id)
        else:
            # If a new task is created, add it to the list
            cached_tasks.append(instance.id)
        cache.set('tasks_list', cached_tasks)
