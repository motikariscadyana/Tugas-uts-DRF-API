from django.db import models

class Category(models.Model):
    jenis = models.CharField(max_length=150)

    def __str__(self):
        return self.jenis
    
class Product(models.Model):
    ukuran = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    harga = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.ukuran 
    
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField()
    date_ordered = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.quantity} x {self.product.ukuran}"
