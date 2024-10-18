from django.contrib import admin
from django.urls import path
from menu.views import example_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("menu/<slug:menu_name>/", example_view, name="menu"),
    path("menu/<slug:menu_name>/<slug:item_slug>/", example_view, name="menu_item"),
]
