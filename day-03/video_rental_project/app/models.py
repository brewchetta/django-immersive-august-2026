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

    # auto_now_add means it will auto add the date when this gets created
    created_at = models.DateTimeField(auto_now_add=True)
    # auto_now means it will auto update the date whenever the row changes
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"VideoTape(id={self.id}, title={self.title})"

# FULL CRUD

# READ DATA
# VideoTape.objects.all() # get all items
# VideoTape.objects.get(pk=1) # get item with id of 1
# VideoTape.objects.get(title="Aladdin") # get item with title of "Aladdin"

# # CREATE DATA
# new_tape = VideoTape(title="Aladdin", runtime_in_minutes=90, rented=False)
# new_tape.save() # commit it to the db with .save()

# # EDIT DATA
# aladdin = VideoTape.objects.get(title="Aladdin") # get item
# aladdin.rented = True # change attribute(s)
# aladdin.save() # commit the change to the db

# # DELETE DATA
# aladdin = VideoTape.objects.get(title="Aladdin") # get item
# aladdin.delete() # delete the row from the db