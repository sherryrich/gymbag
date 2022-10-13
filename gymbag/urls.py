"""gymbag URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from contact.views import contact
from installation.views import Installation
from .views import handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('blogs/', include('blog.urls'), name='news'),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('bag/', include('bag.urls')),
    path('checkout/', include('checkout.urls')),
    path('profile/', include('profiles.urls')),
    path('about/', TemplateView.as_view(template_name="about.html"), name='about'),
    path('privacy/', TemplateView.as_view(template_name="privacy.html"), name='privacy'),
    path('terms/', TemplateView.as_view(template_name="terms.html"), name='terms'),
    path('contact/', contact, name='contact'),
    path('installation/', Installation, name='installation'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = 'gymbag.views.handler404'
