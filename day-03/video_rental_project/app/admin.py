from django.contrib import admin
# pull the VideoTape model from models.py
from .models import VideoTape

# register VideoTape so we can see it in the admin panel
admin.site.register(VideoTape)