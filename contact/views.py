from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.urls import reverse_lazy
from django.views import generic, View
from .forms import ContactForm
from django.forms import Form
from django.http import HttpResponseRedirect
from django.contrib import messages


# Create your views here.

"""View for contact form"""


def contact(request):
    submitted = False
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Your message has been sent sucesfully !' +
                ' We aim to respond within 1 working day.')
            return HttpResponseRedirect('/contact?submitted=True')
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True
    form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})

