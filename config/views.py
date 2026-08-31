"""Project-level views. Application screens live in their own apps."""
from django.shortcuts import render


def home(request):
    """Render the placeholder homepage."""
    return render(request, "home.html")
