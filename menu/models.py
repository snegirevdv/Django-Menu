from django.db import models
from django.utils.text import slugify
from menu.constants import MaxLength


class Item(models.Model):
    name = models.CharField(
        verbose_name="Name",
        max_length=MaxLength.ITEM_NAME,
    )
    slug = models.SlugField(
        verbose_name="Slug",
        max_length=MaxLength.ITEM_SLUG,
        blank=True,
        null=True,
        unique=True,
    )
    menu = models.ForeignKey(
        verbose_name="Menu",
        to="Menu",
        on_delete=models.CASCADE,
        related_name="items",
    )
    parent = models.ForeignKey(
        verbose_name="Parent Item",
        to="self",
        on_delete=models.CASCADE,
        related_name="children",
        null=True,
        blank=True,
    )
    url = models.CharField(
        verbose_name="URL",
        max_length=MaxLength.URL,
        blank=True,
        null=True,
    )
    named_url = models.CharField(
        verbose_name="Named URL",
        max_length=MaxLength.NAMED_URL,
        blank=True,
        null=True,
    )

    class Meta:
        unique_together = ("name", "menu")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)


class Menu(models.Model):
    name = models.SlugField(verbose_name="Slug", max_length=50, unique=True)

    def __str__(self):
        return self.name
