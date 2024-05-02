from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import CompraForm
from .models import ItemCompra, Categoria

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