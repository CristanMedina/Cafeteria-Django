from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem
from menu.models import Cart, CartItem

@login_required
def create_order(request):
    cart = get_object_or_404(Cart, customer=request.user)
    order = Order.objects.create(customer=request.user)
    for item in cart.cartitem_set.all():
        OrderItem.objects.create(order=order, dish=item.dish, quantity=item.quantity)
    cart.cartitem_set.all().delete()
    return redirect('order_list')

@login_required
def order_list(request):
    orders = Order.objects.filter(customer=request.user)
    return render(request, 'orders/order_list.html', {'orders': orders})

@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, customer=request.user)
    return render(request, 'orders/order_detail.html', {'order': order})
