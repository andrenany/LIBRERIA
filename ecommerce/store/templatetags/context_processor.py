from store.models import Cart, CartItem

def cart_context_processor(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)
        total_acumulado = sum(item.subtotal() for item in cart_items)
    else:
        cart_items = []
        total_acumulado = 0

    return {
        'cart': cart,
        'cart_items': cart_items,
        'total_acumulado': total_acumulado,
    }
