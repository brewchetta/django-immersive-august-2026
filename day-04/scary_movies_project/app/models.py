from django.db import models

# model --> bridge b/w your app and the database
# each model represents a table

class Movie(models.Model):
    # mandatory title - max length of 200
    title = models.CharField(max_length=200)
    # optional url to a poster image
    poster_url = models.URLField(null=True, blank=True)

    # timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Movie( pk={self.pk}, title={self.title} )"