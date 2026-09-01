from django import forms
from .models import GamingPC

class GamingPCForm(forms.ModelForm):
    class Meta:
        model = GamingPC
        fields = ['ram', 'cpu', 'gpu']