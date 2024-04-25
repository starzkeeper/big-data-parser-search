from django.db import models


class HeritageLostObject(models.Model):
    date_reg = models.DateField(verbose_name='Дата регистрации')
    reg_number = models.IntegerField(blank=True, null=True, verbose_name='Регистрационный номер')
    name = models.CharField(blank=True, null=True, verbose_name='Название культурной ценности')
    classification = models.CharField(blank=True, null=True, verbose_name='Классификация культурной ценности')
    category = models.CharField(blank=True, null=True, verbose_name='Категория культурной ценности')
    state = models.CharField(blank=True, null=True, verbose_name='Описание состояния сохранности')
    height = models.CharField(blank=True, null=True, verbose_name='Высота')
    width = models.CharField(blank=True, null=True, verbose_name='Ширина')
    length = models.CharField(blank=True, null=True, verbose_name='Длина')
    weight = models.CharField(blank=True, null=True, verbose_name='Вес')

    class Meta:
        managed = False
        db_table = 'heritage_lost_objects'
        verbose_name = 'Утраченная ценность'
        verbose_name_plural = 'Утраченные ценности'
        ordering = ['id']

    def __str__(self):
        return f'ID объекта - {self.id}'
