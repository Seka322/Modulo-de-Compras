from django import forms
from .models import Sucursal, Categoria, ItemCompra

class CompraForm(forms.ModelForm):
	categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), initial=0)
	sucursal = forms.ModelChoiceField(queryset=Sucursal.objects.all(), initial=0)
	class Meta:
		model = ItemCompra
		fields = ['nombre', 'cantidad', 'categoria', 'sucursal']