from uuid import uuid4
from django.db import models

from vps.consts import SERVER_STATUSES


class VPS(models.Model):
    """Модель виртуального сервера."""

    uid = models.UUIDField(
        'уникальный идентификатор сервера',
        primary_key=True,
        default=uuid4,
        editable=False,
    )
    cpu = models.PositiveIntegerField('количество процессорных ядер')
    ram = models.PositiveIntegerField('объем оперативной памяти')
    hdd = models.PositiveIntegerField('объем дискового пространства')
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
