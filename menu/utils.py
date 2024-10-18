from django.urls import NoReverseMatch, reverse

from menu.models import Item


def get_absolute_url(item: Item) -> str:
    """Returns the absolute URL for a given menu item."""
    if item.named_url:
        try:
            return reverse(item.named_url)
        except NoReverseMatch:
            pass

    if item.url:
        return item.url

    return reverse(
        "menu_item",
        kwargs={"menu_name": item.menu.name, "item_slug": item.slug},
    )
