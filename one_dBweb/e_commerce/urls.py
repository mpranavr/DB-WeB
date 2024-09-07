from django.urls import path
from . import views


urlpatterns = [
    # Home page
    path('', views.home, name='home'),

    # User-related URLs
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),

    # Product-related URLs
    path('products/', views.product_list, name='product_list'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),

    # Category-related URLs
    path('categories/', views.category_list, name='category_list'),
    path('categories/<int:category_id>/', views.category_detail, name='category_detail'),

    # Cart-related URLs
    path('cart/', views.cart_view, name='cart_view'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('update_cart/<int:product_id>/', views.update_cart, name='update_cart'),

    # Order-related URLs
    path('orders/', views.order_list, name='order_list'),
    path('orders/<int:order_id>/', views.order_detail, name='order_detail'),

    # Payment-related URLs
    path('payment/', views.payment, name='payment'),

    # Shipping-related URLs
    path('shipping-addresses/', views.shipping_address_list, name='shipping_address_list'),
    path('shipping-addresses/add/', views.shipping_address_add, name='shipping_address_add'),
    path('shipping-addresses/<int:address_id>/', views.shipping_address_detail, name='shipping_address_detail'),

    # Review-related URLs
    path('reviews/add/', views.review_add, name='review_add'),

    # Inventory-related URLs
    path('inventory/', views.inventory_list, name='inventory_list'),

    # Coupon-related URLs
    path('coupons/', views.coupon_list, name='coupon_list'),

    # Static and media files (if needed)
    path('media/<path:path>/', views.serve_media, name='serve_media'),
]
