# from celery import task 
from celery import shared_task
from django_api.celery import app


@app.task()
def test():
    print("Hello Async")