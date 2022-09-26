from django.shortcuts import render
from .forms import InstallationForm
from .models import Installation
from profiles.models import UserProfile
from django.contrib import messages
from django.core.exceptions import ValidationError

# Create your views here.


def Installation(request):
    """ View to return to the Installation page."""
    if request.method == "POST":
        form_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'phone_number': request.POST['phone_number'],
            'email_address': request.POST['email_address'],
            'date': request.POST['date'],
            'installation_type': request.POST['installation_type'],

        }
        form = InstallationForm(form_data)
        if form.is_valid():
            try:
                form.save()
                messages.success(
                    request,
                    "Thanks for submitting your Installation Query" +
                    " We will be in touch to re-confirm your" +
                    " time and date.")
            except ValidationError as e:
                messages.error(request, e.message)

    booking_form = InstallationForm()
    context = {
        'booking_form': booking_form,
    }
    return render(request, 'installation/installation.html', context)