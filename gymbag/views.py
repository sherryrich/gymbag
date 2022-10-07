from django.views.generic import View

class about(View):
    """View for displaying the 'About' page."""
    template_name = "about.html"
