from django.core.management.base import BaseCommand
from menu.models import Menu, Item


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        main_menu = Menu.objects.create(name="main_menu")

        item_1 = Item.objects.create(name="Item 1", menu=main_menu)
        item_2 = Item.objects.create(name="Item 2", menu=main_menu)
        item_3 = Item.objects.create(name="Item 3", menu=main_menu)

        sub_item_1_1 = Item.objects.create(
            name="Item 1.1", menu=main_menu, parent=item_1
        )
        Item.objects.create(name="Item 1.2", menu=main_menu, parent=item_1)
        sub_item_2_1 = Item.objects.create(
            name="Item 2.1", menu=main_menu, parent=item_2
        )

        Item.objects.create(name="Item 1.1.1", menu=main_menu, parent=sub_item_1_1)
        Item.objects.create(name="Item 1.1.2", menu=main_menu, parent=sub_item_1_1)
        Item.objects.create(name="Item 2.1.1", menu=main_menu, parent=sub_item_2_1)

        for i in range(1, 6):
            Item.objects.create(name=f"Item 3.{i}", menu=main_menu, parent=item_3)

        for i in range(1, 4):
            parent_item = Item.objects.create(
                name=f"Item 3.1.{i}",
                menu=main_menu,
                parent=Item.objects.get(name="Item 3.1"),
            )
            for j in range(1, 4):
                Item.objects.create(
                    name=f"Item 3.1.{i}.{j}", menu=main_menu, parent=parent_item
                )

        print("Data has been load succesfully.")
