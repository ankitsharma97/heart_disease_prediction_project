# prediction_app/forms.py
from django import forms
from .models import UserInput

class UserInputForm(forms.ModelForm):
    class Meta:
        model = UserInput
        exclude = ['id']
