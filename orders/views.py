from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Order
from .forms import OrderForm
from django.shortcuts import get_object_or_404
from menu.models import Platillo

class CreateOrderView(LoginRequiredMixin, CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'orders/create_order.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        platillo_id = self.kwargs.get('platillo_id')
        if platillo_id:
            context['platillo'] = get_object_or_404(Platillo, id=platillo_id)
        return context

    def get_initial(self):
        initial = super().get_initial()
        platillo_id = self.kwargs.get('platillo_id')
        if platillo_id:
            initial['platillo'] = platillo_id
        return initial

    def form_valid(self, form):
        form.instance.client = self.request.user
        platillo_id = self.kwargs.get('platillo_id')
        if platillo_id:
            form.instance.platillo = get_object_or_404(Platillo, id=platillo_id)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('orders:order_list')

class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'orders/order_list.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(client=self.request.user).order_by('-created_at')
