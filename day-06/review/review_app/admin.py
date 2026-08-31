from django.contrib import admin
from .models import Review

# this allows us to see/interact with the Review model/table in the admin panel
admin.site.register(Review)

# create a super user using terminal:
# python manage.py createsuperuser