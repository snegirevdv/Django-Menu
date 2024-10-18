from django.http import HttpResponse
from django.shortcuts import render


def example_view(request, menu_name: str, item_slug: str | None = None) -> HttpResponse:
    """Renders the example view with menu."""
    return render(
        request=request,
        template_name="example.html",
        context={"menu_name": menu_name, "item_slug": item_slug},
    )
