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
            'date',
            'installation_type',
        )

    date = forms.DateField(
        widget=forms.widgets.DateInput(
            attrs={
                'type': 'date'}))

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)