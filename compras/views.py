from django.views.generic import CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import CompraForm
from .models import ItemCompra, Categoria
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login
from .forms import RegistroForm

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