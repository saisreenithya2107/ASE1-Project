from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from seller.models import Products_Selling as Product
from .cart import Cart
from .forms import CartAddProductForm
from django.forms import ModelForm
from seller.forms import saleform

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = saleform(instance=product)
    cart.add(product=product)
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['quantity'] = 1
    return render(request, 'cart/detail.html', {'cart': cart})
