"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from api import views as api_views

from django.urls import path, include
from products import views


router = DefaultRouter()
router.register(r'categories', api_views.CategoryViewSet)
router.register(r'products', api_views.ProductViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', views.index, name='index'),
    path('cart/', include('cart.urls'), name='cart'),
    path('accounts/', include('accounts.urls'), name='accounts'),
    path('product/<int:id>/', views.product_detail, name='product'),
    path('shop/', views.shop, name='shop'),
]


if settings.DEBUG:  # Only use this for development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)