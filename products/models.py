from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    customizable = models.BooleanField(default=False)
    options = models.Choices('S', 'M', 'L', 'XL')
    image = models.ImageField(upload_to='images/')
    customizable_image = models.ImageField(upload_to='images/', null=True)
    stock = models.PositiveBigIntegerField()

    def __str__(self):
        return self.name