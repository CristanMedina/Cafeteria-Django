from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Platillo
from .forms import MenuForm

class MenuListView(ListView):
    model = Platillo
    template_name = 'menu/menu_list.html'
    context_object_name = 'platillos'

    def get_queryset(self):
        return Platillo.objects.filter(disponible=True).order_by('nombre')

class MenuCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Platillo
    form_class = MenuForm
    template_name = 'menu/menu_form.html'
    success_url = reverse_lazy('menu:menu_list')

    def test_func(self):
        return self.request.user.role == 'COCINERO'

class MenuUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Platillo
    form_class = MenuForm
    template_name = 'menu/menu_form.html'
    success_url = reverse_lazy('menu:menu_list')

    def test_func(self):
        return self.request.user.role == 'COCINERO'

class MenuDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Platillo
    template_name = 'menu/menu_delete_confirm.html'
    success_url = reverse_lazy('menu:menu_list')

    def test_func(self):
        return self.request.user.role == 'COCINERO'
