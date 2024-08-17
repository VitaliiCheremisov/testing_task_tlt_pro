# Модуль моделей проекта
from django.conf import settings
from django.db import models


class Attr(models.Model):
    """Атрибут."""
    name = models.CharField(
        max_length=settings.MAX_ATTR_NAME_LENTGH,
        verbose_name="Название атрибута"
    )

    class Meta:
        verbose_name = "Атрибут"
        verbose_name_plural = "Атрибуты"

    def __str__(self):
        return self.name


class ProductAttr(models.Model):
    """Переходная таблица связи Продукта с Атрибутом."""
    attr = models.ForeignKey(
        "Attr",
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        "Product",
        on_delete=models.CASCADE
    )
    value = models.CharField(
        max_length=settings.PRODUCT_ATTR_VALUE)



class ProductInterface(models.Manager):
    """Интерфейс работы с моделью Продуктов."""

    def all(self, *args, **kwargs):
        """Вызов всех моделей Продукта."""
        return super().get_queryset().filter(*args, **kwargs)

    def generate(self, product_instance):
        """Создание Уникального продукта."""
        unique_product = self.model.unique_products.create(
            product=product_instance
        )
        return unique_product


class Product(models.Model):
    """Продукт."""
    name = models.CharField(
        max_length=settings.MAX_PRODUCT_NAME_LENTGH,
        verbose_name="Название продукта"
    )
    attrs = models.ManyToManyField(
        "Attr",
        through="ProductAttr")

    objects = ProductInterface()

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def unique_products(self):
        return UniqueProduct.objects.fiter(product=self)

    def __str__(self):
        return self.name


class UniqueProduct(models.Model):
    """Уникальный продукт."""
    product = models.ForeignKey(
        Product,
        related_name="unique_products",
        on_delete=models.PROTECT
    )
    attr = models.ForeignKey(
        ProductAttr,
        on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Уникальный продукт"
        verbose_name_plural = "Уникальные продукты"

    def __str__(self):
        return f"{self.product.name} - {self.attr.value}"
