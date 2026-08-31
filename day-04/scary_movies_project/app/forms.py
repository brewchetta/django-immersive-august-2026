from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        # the model we're basing the form off of
        model = Movie
        # what fields do we want?
        fields = ['title', 'poster_url']