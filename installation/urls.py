from . import views
from django.urls import path, reverse
from django.views.generic import TemplateView

urlpatterns = [
    path('installation/', views.installation, name='installation'),
]