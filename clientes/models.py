from django.db import models
from unittest.util import _MAX_LENGTH

# Create your models here.

class Cliente(models.Model):
    codigo = models.CharField(max_length=200, null=True, blank=True)
    nombre = models.CharField(max_length=200, null=True, blank=True)
    telefono = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

class Meta:
    verbose_name = 'clientes'
    verbose_name_plural = 'clientes'

def __str__(self):
    return self.nombre