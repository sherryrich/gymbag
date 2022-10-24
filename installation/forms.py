from django import forms
from .models import Installation
from django.core.exceptions import ValidationError


class InstallationForm(forms.ModelForm):
    """Form for the Installation model"""
    class Meta:
        model = Installation
        fields = (
            'first_name',
            'last_name',
            'phone_number',
            'email_address',
            'installation_type',
            'date',
        )
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'email_address': forms.EmailInput(attrs={'class': 'form-control'}),
            'installation_type': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.SelectDateWidget(attrs={'class': 'form-control'}),
        }

    date = forms.DateField(
        widget=forms.widgets.DateInput(
            attrs={
                'type': 'date'}))

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
