from django.urls import path
from .views import KitchenOrderListView, OrderStatusUpdateView

app_name = 'kitchen_orders'

urlpatterns = [
    path('', KitchenOrderListView.as_view(), name='kitchen_dashboard'),
    path('<int:pk>/update/', OrderStatusUpdateView.as_view(), name='update_status'),
]
