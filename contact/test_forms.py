from django.test import TestCase
from .forms import ContactForm


class TestItemForm(TestCase):

    def test_item_name_is_required(self):
        form = ContactForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(
            form.errors['name'][0], 'This field is required.'
        )

    def test_fields_are_explicit_in_form_metaclass(self):
        form = ContactForm()
        self.assertEqual(
            form.Meta.fields, '__all__')
