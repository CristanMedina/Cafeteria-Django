from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, UpdateView
from orders.models import Order
from django.urls import reverse_lazy

class KitchenOrderListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Order
    template_name = 'kitchen_orders/order_list.html'
    context_object_name = 'orders'
    ordering = ['-created_at']  # Newest first

    def test_func(self):
        return self.request.user.role == 'COCINERO'

class OrderStatusUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Order
    fields = ['status']
    template_name = 'kitchen_orders/order_status_update.html'
    success_url = reverse_lazy('kitchen_orders:kitchen_dashboard')

    def test_func(self):
        return self.request.user.role == 'COCINERO'
