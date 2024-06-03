from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def _str_(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def _str_(self):
        return self.name
