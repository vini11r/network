from django.db import models


class Element(models.Model):
    LEVEL = [
        (0, "Завод"),
        (1, "Розничная сеть"),
        (2, "Индивидуальный предприниматель"),
    ]

    name = models.CharField(max_length=150, verbose_name="Название")
    email = models.EmailField(
        unique=True, max_length=255, verbose_name="Почта", help_text="Укажите почту"
    )
    country = models.CharField(
        max_length=100, verbose_name="Страна", blank=True, null=True
    )
    city = models.CharField(max_length=100, verbose_name="Город", blank=True, null=True)
    street = models.CharField(
        max_length=100, verbose_name="Улица", blank=True, null=True
    )
    number_house = models.ImageField(verbose_name="Номер дома", blank=True, null=True)
    network_level = models.IntegerField(verbose_name="Уровень сети", choices=LEVEL)
    shipper = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        verbose_name="Поставщик",
        blank=True,
        null=True,
    )
    debt = models.DecimalField(
        max_digits=11,
        decimal_places=2,
        default=0.00,
        verbose_name="Задолженность перед поставщиком, руб.",
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Время и дата создания"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Элемент сети"
        verbose_name_plural = "Элементы сети"


class Product(models.Model):
    shipper = models.ForeignKey(
        Element, verbose_name="Поставщик", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=150, verbose_name="Название продукта")
    release_date = models.DateField(verbose_name="Дата выхода продукта на рынок")
    product_model = models.CharField(max_length=100, verbose_name="Модель продукта", blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.product_model}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
