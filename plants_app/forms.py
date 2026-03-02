from django import forms
from .models import Plant, Care

class CareForm(forms.ModelForm): 
    class Meta: 
        model = Care 
        fields = ['date', 'care_type']

        widgets= {
            'date': forms.DateInput(
                attrs={
                    'type': 'text', 
                    'placeholder': 'YYYY-MM-DD', 
                    'class': 'datepicker'
                }
            )
        }