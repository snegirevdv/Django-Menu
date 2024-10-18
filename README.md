# Django Menu

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Loading Test Data](#loading-test-data)
- [Admin Interface](#admin-interface)
- [Menu Rendering](#menu-rendering)
- [URL Logic](#url-logic)

This project is a Django-based application for managing menus. It provides a flexible structure for creating and organizing hierarchical menus with multiple levels of items.

## Features

- Create and manage menus through the admin interface.
- Organize items in a hierarchical structure, allowing nested items.
- Dynamic rendering of menus in templates, providing flexibility to show or hide menu items based on the current page or user context.
- Customizable template tags to integrate menus seamlessly into your site's design.
- Support for multi-level menus, enabling creation of both simple and deeply nested menu structures.

### Requirements

- Python 3.10+

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/snegirevdv/Django-Menu.git
   cd Django-Menu
   ```

2. Install the required packages:

   #### Using Poetry

   ```sh
   poetry install
   ```

   #### Using pip

   ```sh
   pip install -r requirements.txt
   ```

3. Apply database migrations:

   ```sh
   python manage.py migrate
   ```

4. Create a superuser to access the Django admin:

   ```sh
   python manage.py createsuperuser
   ```

5. Run the development server:

   ```sh
   python manage.py runserver
   ```

6. Access the application in your browser at `http://127.0.0.1:8000/`.

## Loading Test Data

To populate the database with test data, you can use the management command `python manage.py loat_test_data`.
This command will create a sample menu structure with multiple levels of items.

## Admin Interface

The admin interface is provided to manage the menus and items. You can:

- View and edit menus
- View and edit items, including children items directly

To access the admin interface, navigate to `http://127.0.0.1:8000/admin/` and use the superuser credentials you created earlier.

## Menu Rendering

To render a menu in your templates, you can use the custom template tag `draw_menu`.

1. Load the `menu_extras` template tag library:

   ```html
   {% load menu_extras %}
   ```

2. Use the `draw_menu` tag to render a menu by its name:

   ```html
   {% draw_menu 'main_menu' %}
   ```

3. This will include the template `menu/draw_menu.html` to render the menu structure.

## URL Logic

The URL for menu items can be specified in different ways:

- **Named URL**: If the item has a `named_url`, the app attempts to resolve it using Django's `reverse()` function. This is useful for dynamically linking to other views within your Django project.
- **Custom URL**: If a `named_url` is not provided but the item has a `url` attribute, it will use that as the link. This allows for linking to external or custom URLs.
- **Default URL Format**: If neither `named_url` nor `url` is specified, the URL will be constructed in the format `/menu/<menu_name>/<item_slug>/`. This allows for a default structure that can be useful for testing or for basic menu navigation.
