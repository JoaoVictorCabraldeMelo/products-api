from django.db import models
from django.utils.translation import gettext_lazy as _



class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()

    class Status(models.TextChoices):
        ATIVO = 'ativo', _('ativo')
        INATIVO = 'inativo', _('inativo')
    
    status = models.CharField(max_length=7, choices=Status.choices, default=Status.INATIVO)

    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name
