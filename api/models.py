from django.db import models
from simple_history.models import HistoricalRecords


class Clothes(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=255)
    article = models.IntegerField(verbose_name='Артикул')
    manufacturer = models.ForeignKey("Manufacturer", verbose_name='Производитель', on_delete=models.CASCADE)
    category = models.ManyToManyField("Category", verbose_name='Категория')
    price = models.PositiveIntegerField(verbose_name='Цена')
    amount = models.PositiveIntegerField(verbose_name='Количество')

    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вещь'
        verbose_name_plural = 'Вещи'


class Category(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=255)
    description = models.TextField(verbose_name='Описание')

    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Manufacturer(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=255)
    description = models.TextField(verbose_name='Описание')
    address = models.TextField(verbose_name='Адрес')

    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'
