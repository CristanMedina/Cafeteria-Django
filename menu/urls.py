from django.urls import path
from .views import menu_list, add_to_cart, cart_detail

urlpatterns = [
    path('', menu_list, name='menu_list'),
    path('cart/', cart_detail, name='cart_detail'),
    path('add/<int:dish_id>/', add_to_cart, name='add_to_cart'),
]
