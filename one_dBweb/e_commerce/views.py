from django.shortcuts import render, get_object_or_404, redirect
from .models import Products, Categories, Orders, ShippingAddresses, Reviews, Inventory, Coupons
from .forms import ReviewForm, ShippingAddressForm
from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Automatically log the user in after registration
            return redirect('product_list')  # Redirect to the product list page
    else:
        form = UserCreationForm()
    
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('product_list')  # Redirect to the product list page
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('home')

@login_required
def profile(request):
    return render(request, 'profile.html')

def product_list(request):
    products = Products.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Products, product_id=product_id)
    return render(request, 'product_detail.html', {'product': product})

def category_list(request):
    categories = Categories.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def category_detail(request, category_id):
    category = get_object_or_404(Categories, pk=category_id)
    products = Products.objects.filter(category=category)
    return render(request, 'category_detail.html', {'category': category, 'products': products})

def cart_view(request):
    # Retrieve cart items from the session
    cart = request.session.get('cart', {})
    
    # Retrieve product details for each item in the cart
    cart_items = []
    total_price = 0
    
    for product_id, quantity in cart.items():
        product = Products.objects.get(id=product_id)
        item_total = product.price * quantity
        total_price += item_total
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'item_total': item_total
        })
    
    context = {
        'cart_items': cart_items,
        'total_price': total_price
    }
    
    return render(request, 'cart_view.html', context)

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    
    if product_id in cart:
        cart[product_id] += 1
    else:
        cart[product_id] = 1
    
    request.session['cart'] = cart
    return redirect('cart_view')

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    
    if product_id in cart:
        del cart[product_id]
    
    request.session['cart'] = cart
    return redirect('cart_view')

def update_cart(request, product_id):
    quantity = int(request.POST.get('quantity', 0))
    cart = request.session.get('cart', {})
    
    if quantity > 0:
        cart[product_id] = quantity
    else:
        if product_id in cart:
            del cart[product_id]
    
    request.session['cart'] = cart
    return redirect('cart_view')

def order_list(request):
    orders = Orders.objects.filter(user_id=request.user.user_id)
    return render(request, 'order_list.html', {'orders': orders})

def order_detail(request, order_id):
    order = get_object_or_404(Orders, pk=order_id)
    return render(request, 'order_detail.html', {'order': order})

def payment(request):
    # Implement payment logic here
    pass

def shipping_address_list(request):
    addresses = ShippingAddresses.objects.filter(user=request.user)
    return render(request, 'shipping_address_list.html', {'addresses': addresses})

def shipping_address_add(request):
    if request.method == 'POST':
        form = ShippingAddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            return redirect('shipping_address_list')
    else:
        form = ShippingAddressForm()
    return render(request, 'shipping_address_add.html', {'form': form})

def shipping_address_detail(request, address_id):
    address = get_object_or_404(ShippingAddresses, pk=address_id)
    return render(request, 'shipping_address_detail.html', {'address': address})

def review_add(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('product_list')
    else:
        form = ReviewForm()
    return render(request, 'review_add.html', {'form': form})

def inventory_list(request):
    inventory_items = Inventory.objects.all()
    return render(request, 'inventory_list.html', {'inventory_items': inventory_items})

def coupon_list(request):
    coupons = Coupons.objects.all()
    return render(request, 'coupon_list.html', {'coupons': coupons})

def serve_media(request, path):
    # Handle media files if needed
    pass
