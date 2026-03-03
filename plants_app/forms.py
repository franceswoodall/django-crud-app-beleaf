from django import forms
from .models import Care
from datetime import date 

class CareForm(forms.ModelForm): 
    class Meta: 
        model = Care 
        fields = ['date', 'care_type', 'time_of_day']

        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date', 
                    'value': date.today()
                }
            ),
        }