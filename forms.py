from django import forms
from .models import hello

class helloForm(forms.ModelForm):
    class Meta:
        model = hello
        fields = ['name', 'date', 'time', 'email', 'active']
    widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            }

