from django import forms
from .models import GamingPC, Headphone

class GamingPCForm(forms.ModelForm):
    class Meta:
        model = GamingPC
        fields = ['ram', 'cpu', 'gpu']

class HeadphoneForm(forms.ModelForm):
    class Meta:
        model = Headphone
        fields = ['brand', 'price']