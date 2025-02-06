from django.urls import path
from . import  views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('cart_total/', views.total, name='cart_total'),
    path('add/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:id>/', views.remove_from_cart, name='remove_from_cart'),
    path('quantity/<int:id>/', views.quantity, name='quantity'),
    path('clear/', views.clear_cart, name='clear_cart'),
    path('count/', views.cart_count, name='cart_count'),
    
]