from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register


urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
]