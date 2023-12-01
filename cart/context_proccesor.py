from .models import Cart, CartItem
from .views import _cart_id

def counter(request):
    item_count = 0
    
    if 'admin' in request.path:
        return {}
    
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart)
        item_count = sum(cart_item.quantity for cart_item in cart_items)
    except Cart.DoesNotExist:
        item_count = 0

    return {'item_count': item_count}
