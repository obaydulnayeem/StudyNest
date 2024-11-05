from django import forms
from . models import *

class WelcomeForm(forms.ModelForm):
    class Meta:
        model = WelcomeModel
        fields = '__all__'