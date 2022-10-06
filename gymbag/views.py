from django.shortcuts import render


class about(View):
    """View for displaying the 'About' page."""
    template_name = "about.html"


def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, "errors/404.html", status=404)