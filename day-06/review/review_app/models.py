from django.db import models
from django.contrib.auth import get_user_model

# refers to the user model/table
User = get_user_model()

class Review(models.Model):
    # foreign key linking review to a specific user
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    # the written content for the review
    content = models.TextField()
    # add timestamps automatically
    created_at = models.DateTimeField( auto_now_add=True )
    updated_at = models.DateTimeField( auto_now=True )