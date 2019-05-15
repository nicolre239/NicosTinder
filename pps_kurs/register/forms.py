from django import forms
from .models import *

class RegFrom(forms.ModelForm):

    class Meta:
        model = User
        exclude=[""]