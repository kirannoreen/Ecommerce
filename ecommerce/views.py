from django.shortcuts import render, get_object_or_404, redirect
from .models import Product

# Create your views here.

def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, "home.html", context)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'product_detail.html', context)

def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart = request.session.get('cart', {})
    
    # For simplicity, we'll handle quantity from a form input.
    quantity = int(request.POST.get('quantity', 1))
    cart[str(pk)] = cart.get(str(pk), 0) + quantity
    
    request.session['cart'] = cart
    return redirect('cart')

def remove_from_cart(request, pk):
    cart = request.session.get('cart', {})
    if str(pk) in cart:
        del cart[str(pk)]
    request.session['cart'] = cart
    return redirect('cart')

def cart(request):
    cart_session = request.session.get('cart', {})
    cart_items = []
    cart_total = 0
    
    for product_id, quantity in cart_session.items():
        product = get_object_or_404(Product, pk=product_id)
        item_total = product.price * quantity
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'total': item_total,
        })
        cart_total += item_total
        
    context = {
        'cart_items': cart_items,
        'cart_total': cart_total,
    }
    return render(request, 'cart.html', context)

def checkout(request):
    # The checkout page also needs the cart contents to display an order summary
    cart_session = request.session.get('cart', {})
    cart_items = []
    cart_total = 0
    
    for product_id, quantity in cart_session.items():
        product = get_object_or_404(Product, pk=product_id)
        cart_items.append({'product': product, 'quantity': quantity})
        cart_total += product.price * quantity
        
    context = {'cart_items': cart_items, 'cart_total': cart_total}
    return render(request, 'payment.html', context)
