from django.test import TestCase
from .models import Contact


class TestItemForm(TestCase):

    def test_item_string_method_returns_name(self):
        form = Contact.objects.create(name='test item')
        self.assertEqual(str(form), 'test item')
