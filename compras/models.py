from django.db import models
from django.contrib.auth.models import User

class ItemCompra(models.Model):
	sucursal = models.ForeignKey('Sucursal', on_delete=models.SET_NULL, blank=True, null=True)
	producto = models.CharField(max_length=255)
	proveedor = models.CharField(max_length=255)
	unidades = models.IntegerField()
	minimo_unidades = models.IntegerField()
	costo = models.DecimalField(max_digits=10, decimal_places=2)
	cantidad = models.IntegerField()
	fecha_orden = models.DateTimeField(auto_now_add=True)
	fecha_entrega = models.DateTimeField()

	def __str__(self):
		return self.producto
	
	
class Sucursal(models.Model):
	nombre = models.CharField(max_length=200)
	direccion = models.CharField(max_length=200)

	def __str__(self):
		return self.nombre
	
class ItemProveedor(models.Model):
	item = models.CharField(max_length=255)
	proveedor = models.CharField(max_length=255)
	cantidad_por_unidad = models.CharField(max_length=100)
    unidades = models.IntegerField()