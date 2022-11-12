from django.db import models


class Contact(models.Model):
    REASON_FOR_CONTACT = [
        ('please select', 'Please select'),
        ('returns', 'Returns'),
        ('availability', 'Availability'),
        ('pricing', 'Pricing'),
        ('feedback', 'Feedback'),
        ('other', 'Other'),
    ]
    name = models.CharField(
        max_length=80
        )
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(
        auto_now_add=True
        )
    contact_reason = models.CharField(
        max_length=24,
        choices=REASON_FOR_CONTACT,
        default='please select below'
        )
    def __str__(self):
        return self.name
