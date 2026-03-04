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
                    'class': 'form-input', 
                    'placeholder': 'Select a date',
                    'type': 'date', 
                    'value': date.today()
                }
            ),
            'care_type': forms.Select(attrs={'class': 'form-input'}),
            'time_of_day': forms.Select(attrs={'class': 'form-input'}), 
        }