from uuid import uuid4
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from vps.consts import MAX_CPU, MAX_HDD, MAX_RAM, SERVER_STATUSES


class VPS(models.Model):
    """Модель виртуального сервера."""

    uid = models.UUIDField(
        'уникальный идентификатор сервера',
        primary_key=True,
        default=uuid4,
        editable=False,
    )
    cpu = models.PositiveIntegerField(
        'количество процессорных ядер',
        validators=[MinValueValidator(1), MaxValueValidator(MAX_CPU)],
    )
    ram = models.PositiveIntegerField(
        'объем оперативной памяти',
        validators=[MinValueValidator(1), MaxValueValidator(MAX_RAM)],
    )
    hdd = models.PositiveIntegerField(
        'объем дискового пространства',
        validators=[MinValueValidator(1), MaxValueValidator(MAX_HDD)],
    )
    status = models.CharField(
        'текущий статус сервера',
        max_length=16,
        choices=SERVER_STATUSES,
        default='stopped',
    )

    class Meta:
        verbose_name = 'сервер'
        verbose_name_plural = 'Сервера'

    def __str__(self) -> str:
        return f'Сервер {self.uid}'
