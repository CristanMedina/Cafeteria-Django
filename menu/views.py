from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Dish, Cart, CartItem

def menu_list(request):
    dishes = Dish.objects.all()
    return render(request, 'menu/menu_list.html', {'dishes': dishes})

@login_required
def add_to_cart(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)
    cart, created = Cart.objects.get_or_create(customer=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, dish=dish)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart_detail')

@login_required
def cart_detail(request):
    cart, _ = Cart.objects.get_or_create(customer=request.user)
    return render(request, 'menu/cart_detail.html', {'cart': cart})
