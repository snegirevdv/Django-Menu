from django.contrib import admin
from menu.models import Menu, Item


class ChildItemInline(admin.TabularInline):
    model = Item
    fk_name = "parent"
    extra = 1
    verbose_name = "Item"
    verbose_name_plural = "Nested Items"


class MenuItemInline(admin.TabularInline):
    model = Item
    fk_name = "menu"
    extra = 1
    verbose_name = "Item"
    verbose_name_plural = "Items"


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    inlines = [MenuItemInline]


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "menu", "parent", "url", "named_url")
    list_filter = ("menu", "parent")
    search_fields = ("name",)
    inlines = [ChildItemInline]
