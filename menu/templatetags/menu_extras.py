from django import template
from django.http import HttpRequest
from menu.models import Menu
from menu.tree import MenuTree

register = template.Library()


@register.inclusion_tag("menu/draw_menu.html", takes_context=True)
def draw_menu(context: dict, menu_name: str) -> dict[str, dict]:
    """
    Renders a menu by its name and passes it to the template.

    Example:
        In your Django template, you can use this tag that way:
        {% load menu_extras %}
        {% draw_menu 'main-menu' %}
    """

    request: HttpRequest = context["request"]
    current_url = request.path

    try:
        menu = Menu.objects.get(name=menu_name)
        tree = MenuTree.from_model(menu)
        tree.activate_by_url(current_url)
        menu_dict = tree.to_dict()

    except Menu.DoesNotExist:
        menu_dict = {}

    return {"menu": menu_dict}
