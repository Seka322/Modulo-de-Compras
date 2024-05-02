from django.views.generic import View, CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import CompraForm, RegistroForm
from .models import ItemCompra, Categoria
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

class Inicio(TemplateView):
	template_name = 'welcome.html'

class CrearOrden(LoginRequiredMixin, CreateView):
	model = ItemCompra
	form_class = CompraForm
	template_name = 'order.html'
	success_url = reverse_lazy('dashboard')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['categorias'] = Categoria.objects.all()
		return context

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)

class Dashboard(LoginRequiredMixin, View):
	def get(self, request):
		items = ItemCompra.objects.filter(usuario=self.request.user.id).order_by('id')

		low_inventory = ItemCompra.objects.filter(
			usuario=self.request.user.id,
			cantidad__lte=3
		)

		if low_inventory.count() > 0:
			if low_inventory.count() > 1:
				messages.error(request, f'{low_inventory.count()} items tienen bajo inventario')
			else:
				messages.error(request, f'{low_inventory.count()} item tiene bajo inventario')

		low_inventory_ids = ItemCompra.objects.filter(
			usuario=self.request.user.id,
			cantidad__lte=3
		).values_list('id', flat=True)

		return render(request, 'dashboard.html', {'items': items, 'low_inventory_ids': low_inventory_ids})

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
			return redirect('')

		return render(request, 'signup.html', {'form': form})