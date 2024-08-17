# Модуль админки модели продуктов.
from django.conf import settings
from django.contrib import admin

from .models import Attr, Product, UniqueProduct

@admin.register(Attr)
class ProductAdmin(admin.ModelAdmin):
    """Админ зона Продукта."""

    list_display = ("name",)
    empty_value_display = settings.EMPTY_VALUE
    list_filter = ("name",)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Админ зона Продукта."""

    list_display = ("name",)
    empty_value_display = settings.EMPTY_VALUE
    list_filter = ("name",)

@admin.register(UniqueProduct)
class ProductAdmin(admin.ModelAdmin):
    """Админ зона Продукта."""

    list_display = ("product",)
    empty_value_display = settings.EMPTY_VALUE
    list_filter = ("product",)
