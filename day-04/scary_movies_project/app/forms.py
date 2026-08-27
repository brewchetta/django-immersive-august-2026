from django import forms

class MovieForm(forms.Form):
    title = forms.CharField(max_length=200)
    poster_url = forms.URLField()