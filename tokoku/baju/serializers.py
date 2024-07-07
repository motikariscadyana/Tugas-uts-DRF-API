from rest_framework import serializers
from .models import Kategori, Merek, Pakaian, Pembeli

class KategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategori
        fields = '__all__'

class MerekSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merek
        fields = '__all__'

class PakaianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pakaian
        fields = ['id', 'nama', 'kategori', 'merek', 'kategori_id', 'merek_id', 'harga', 'stok']
    
    kategori = KategoriSerializer(read_only=True)
    merek = MerekSerializer(read_only=True)
    kategori_id = serializers.PrimaryKeyRelatedField(queryset=Kategori.objects.all(), source='kategori', write_only=True)
    merek_id = serializers.PrimaryKeyRelatedField(queryset=Merek.objects.all(), source='merek', write_only=True)

class PembeliSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pembeli
        fields = ['id', 'nama', 'email', 'alamat']