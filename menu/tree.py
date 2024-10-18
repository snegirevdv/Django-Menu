from typing import Self

from menu.models import Item, Menu
from menu.utils import get_absolute_url


class MenuItem:
    """Represents a single menu item with potential child items and an active state."""

    def __init__(self, name: str, url: str | None):
        self.name = name
        self.url = url
        self.children: list[Self] = []
        self.is_active: bool = False

    @classmethod
    def from_model(cls, item: Item) -> Self:
        """Creates a MenuItem instance from a database model."""
        url = get_absolute_url(item)
        menu_item = cls(name=item.name, url=url)

        for child in item.children.all():
            menu_item.add_child(cls.from_model(child))

        return menu_item

    def add_child(self, child: Self) -> None:
        """Adds a child MenuItem to the item."""
        self.children.append(child)

    def activate(self):
        """Activates the menu item, setting its active state to True."""
        self.is_active = True

    def to_dict(self) -> dict | None:
        """Converts the menu item and its children into a dictionary if the item is active."""
        if not self.is_active:
            return None

        return {
            "name": self.name,
            "url": self.url,
            "children": [child.to_dict() for child in self.children if child.is_active],
        }


class MenuTree:
    """Represents the menu tree."""

    def __init__(self, name: str) -> None:
        self.root = MenuItem(name=name, url=None)
        self.root.activate()

    @classmethod
    def from_model(cls, menu: Menu) -> Self:
        """Creates a MenuTree instance from a Menu model."""
        menu_tree = cls(name=menu.name)

        for item in menu.items.filter(parent__isnull=True):
            menu_tree.root.add_child(MenuItem.from_model(item))

        for child in menu_tree.root.children:
            child.activate()

        return menu_tree

    def find_parent(
        self,
        current_item: MenuItem,
        target_item: MenuItem,
    ) -> MenuItem | None:
        """Recursively finds the parent of a given item."""
        for child in current_item.children:
            if child == target_item:
                return current_item

            parent = self.find_parent(child, target_item)

            if parent:
                return parent

    def activate_path(self, target_item: MenuItem) -> None:
        """Activates the path of the target menu item, including its parent and sibling items."""

        current_item: MenuItem | None = target_item

        while current_item:
            current_item.activate()

            for child in current_item.children:
                child.activate()

            current_item = self.find_parent(self.root, current_item)

    def find_node_by_url(self, current_node: MenuItem, url: str) -> MenuItem | None:
        """Recursively finds a node by its URL."""
        if current_node.url == url:
            return current_node

        for child in current_node.children:
            found_node = self.find_node_by_url(child, url)

            if found_node:
                return found_node

    def activate_by_url(self, url: str):
        """Activates the menu items by the given URL."""
        target_item = self.find_node_by_url(self.root, url)

        if target_item and target_item is not self.root:
            self.activate_path(target_item)

    def to_dict(self):
        """Converts the MenuTree to a dictionary representation, including only active items."""
        return self.root.to_dict()
