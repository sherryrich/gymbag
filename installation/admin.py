from django.contrib import admin
from .models import Installation
# Register your models here.

class InstallationAdmin(admin.ModelAdmin):
    """This class defines admin page for the Installation Service"""
    readonly_fields = ('date',)
    fields = ('first_name', 'last_name', 'installation_type',)
    list_display = ('first_name', 'last_name', 'date', 'installation_type')
    ordering = ('-date',)


admin.site.register(Installation, InstallationAdmin)