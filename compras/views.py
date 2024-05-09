from django.views.generic import View, CreateView, TemplateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import CompraForm, RegistroForm
from .models import ItemCompra, ItemProveedor
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.db.models import F

class Inicio(TemplateView):
	template_name = 'welcome.html'

class CrearOrden(LoginRequiredMixin, CreateView):
	model = ItemCompra
	form_class = CompraForm
	template_name = 'order.html'
	success_url = reverse_lazy('dashboard')

	def get_form_kwargs(self):
		kwargs = super().get_form_kwargs()
		kwargs['productos'] = ItemProveedor.objects.exclude(unidades=0)
		return kwargs
	
	def form_valid(self, form):
		form.instance.user = self.request.user
		response = super().form_valid(form)
		producto = form.cleaned_data['producto']
		cantidad = form.cleaned_data['cantidad']
		ItemProveedor.objects.filter(item=producto).update(unidades=F('unidades') - cantidad)
		return response
	
class Dashboard(LoginRequiredMixin, View):
	def get(self, request):
		items = ItemCompra.objects.order_by('id')
		return render(request, 'dashboard.html', {'items': items})

class Registro(View):
	def get(self, request):
		form = RegistroForm()
		return render(request, 'signup.html', {'form': form})

	def post(self, request):
		form = RegistroForm(request.POST)

		if form.is_valid():
			form.save()
			user = authenticate(
				username=form.cleaned_data['username'],
				password=form.cleaned_data['password1']
			)

			login(request, user)
			return redirect('dashboard')

		return render(request, 'signup.html', {'form': form})

def DetallesItem(request, item_id):
    item = ItemProveedor.objects.filter(pk=item_id).first()
    if item:
        data = {
            'proveedor': item.proveedor if item.proveedor else '',
            'unidades': item.unidades,
            'minimo_unidades': item.minimo_unidades,
            'costo': item.costo,
        }
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Item no encontrado'}, status=404)

class CancelarOrden(LoginRequiredMixin, DeleteView):
	def post(self, request, *args, **kwargs):
		item = ItemCompra.objects.get(pk=kwargs['pk'])
		producto = item.producto
		cantidad = item.cantidad
		ItemProveedor.objects.filter(item=producto).update(unidades=F('unidades') + cantidad)
		return super().delete(request, *args, **kwargs)

	model = ItemCompra
	template_name = 'delete.html'
	success_url = reverse_lazy('dashboard')
	context_object_name = 'item'