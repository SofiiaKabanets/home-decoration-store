from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, CartItem
from shop.models import Product

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    
    # Assuming you are getting quantity and update from the request, modify this part accordingly
    quantity = int(request.POST.get('quantity', 1))
    update_quantity = bool(request.POST.get('update', False))
    
    cart.add(product=product, quantity=quantity, update_quantity=update_quantity)
    
    return redirect('cart:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})


