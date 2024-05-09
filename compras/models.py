from django.db import models
from django.contrib.auth.models import User

class ItemCompra(models.Model):
	
	cantidad = models.IntegerField()
	sucursal = models.ForeignKey('Sucursal', on_delete=models.SET_NULL, blank=True, null=True)
	
	def __str__(self):
		return self.nombre
	
class Categoria(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.nombre
	
class Sucursal(models.Model):
	nombre = models.CharField(max_length=200)
	direccion = models.CharField(max_length=200)

	def __str__(self):
		return self.nombre
	