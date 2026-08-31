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


class UserProfile(models.Model):
    profile_img = models.URLField(null=True, blank=True)
    # we could add as many profile attributes as we want
    # associate UserProfile with User
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

# post_save can listen and hear when a user is created or saved
from django.db.models.signals import post_save
# receiver decorator allows us to trigger off of a signal such as post_save
from django.dispatch import receiver

# when a User is saved, the receiver activates
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    # if user was created...
    if created:
        # create and save a new user profile
        profile = UserProfile(user=instance)
        # instance is the newly saved user
        profile.save()