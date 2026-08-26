from django.contrib import admin
# pull the VideoTape model from models.py
from .models import VideoTape, RentalStore, Customer
from .models import School, Teacher, Student

# register VideoTape so we can see it in the admin panel
admin.site.register(VideoTape)
admin.site.register(RentalStore)
admin.site.register(Customer)

admin.site.register(School)
admin.site.register(Teacher)
admin.site.register(Student)