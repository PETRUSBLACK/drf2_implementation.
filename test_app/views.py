from .models import Blog, Car 
from django_seed import Seed

car_names = ("Mercedes", "Toyota", "Audu", "Honday", "Nissan", )

seeder = Seed.seeder()

seeder.add_entity(Blog, 20)

def execute():
    seeder.execute()
    print("seeding completed")