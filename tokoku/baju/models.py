from django.db import models

class Kategori(models.Model):
    nama = models.CharField(max_length=100)

    def __str__(self):
        return self.nama

class Merek(models.Model):
    nama = models.CharField(max_length=100)

    def __str__(self):
        return self.nama

class Pakaian(models.Model):
    nama = models.CharField(max_length=100)
    kategori = models.ForeignKey(Kategori, related_name='pakaian', on_delete=models.CASCADE)
    merek = models.ForeignKey(Merek, related_name='pakaian', on_delete=models.CASCADE)
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    stok = models.PositiveIntegerField()

    def __str__(self):
        return self.nama
