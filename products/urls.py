from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/', views.product_detail),
    path('customizer/<int:id>', views.customizer, name='customizer'),
]