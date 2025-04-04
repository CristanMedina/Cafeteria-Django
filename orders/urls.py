from django.urls import path
from .views import CreateOrderView, OrderListView

app_name = 'orders'

urlpatterns = [
    path('new/', CreateOrderView.as_view(), name='create_order'),
    path('new/<int:platillo_id>/', CreateOrderView.as_view(), name='create_order_with_dish'),
    path('mine/', OrderListView.as_view(), name='order_list'),
]
