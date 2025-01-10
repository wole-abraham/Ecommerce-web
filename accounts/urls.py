from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import signin


urlpatterns = [
    path('login/', signin, name='login'),
    # path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
]