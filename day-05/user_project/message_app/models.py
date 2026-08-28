from django.db import models
from django.contrib.auth import get_user_model

# imports the user model for us using a special, safe function
User = get_user_model()

class Message(models.Model):
    content = models.TextField()
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_messages")
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_messages")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # THERE ARE TWO FOREIGN KEYS
    # one points to the sender and one points to the recipient
    # if either user is deleted, their sent / received messages are deleted as well