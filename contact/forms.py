from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """ Form for the contact model """
    class Meta:
        model = Contact
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_reason': forms.Select(attrs={'class': 'form-control'}),
        }
