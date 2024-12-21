from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    """
        Model: UserProfile
        user: OneToONeField -> each (user)UserModel has one profile
        address: 
        phone:

    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField()
    phone = models.CharField(max_length=16)
    
