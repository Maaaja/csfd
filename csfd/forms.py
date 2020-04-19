from django.db import models
from django import forms


class UvodniForm(forms.Form):
    form = forms.CharField(label='Vyhledej', max_length=100)