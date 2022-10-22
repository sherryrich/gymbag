from django.db import models
import datetime
from django.core.exceptions import ValidationError

# Create your models here.



class Installation(models.Model):
    """Model for installation service"""
    first_name = models.CharField(max_length=60, null=False, blank=False)
    last_name = models.CharField(max_length=60, null=False, blank=False)
    email_address = models.CharField(max_length=60, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    date = models.DateField(default=datetime.date.today())
    INSTALLATION_CHOICES = [
        ('Club', 'Club'),
        ('Corporate', 'Corporate'),
        ('Hotel', 'Hotel'),

    ]
    installation_type = models.CharField(
        max_length=40,
        choices=INSTALLATION_CHOICES,
        default='Club',
    )

    def save(self, *args, **kwargs):
        if self.date < datetime.date.today():
            raise ValidationError("The date cannot be in the past!")
        super(Installation, self).save(*args, **kwargs)
