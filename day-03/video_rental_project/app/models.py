from django.db import models


# a video tape BELONGS TO a rental store
# a rental store HAS MANY video tapes
class RentalStore(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return f"RentalStore(id={self.id}, name={self.name})"

class Customer(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    rental_stores = models.ManyToManyField(RentalStore, blank=True)

    def __str__(self):
        return f"Customer(id={self.id}, name={self.name})"


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
    # associates the video tape to a rental store - a video tape belongs to a store and a store has many tapes
    rental_store = models.ForeignKey(RentalStore, on_delete=models.CASCADE, related_name="video_tapes", null=True, blank=True)

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


class School(models.Model):
    name = models.CharField(max_length=200)
    website = models.URLField(max_length=300)

class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200, null=True, blank=True)
    # teacher belongs to one school
    # school has many teachers
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="teachers")

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    # students can have a blank gpa bc of blank=True/null=True
    gpa = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    # teachers have many students
    # students have many teachers
    teachers = models.ManyToManyField(Teacher, blank=True, related_name="students")