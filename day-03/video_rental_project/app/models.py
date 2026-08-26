from django.db import models

# class - object oriented programming
# instance - an item in the database
class VideoTape(models.Model):
    # VideoTape will have an id by default
    # title is a new column in the db - text - max length 100 characters
    title = models.CharField(max_length=100)
    # runtime is a column - integer
    runtime_in_minutes = models.IntegerField()
    # rented is a column - boolean (true / false)
    rented = models.BooleanField()

    def __str__(self):
        return f"VideoTape(id={self.id}, title={self.title})"