from rest_framework import viewsets
from .models import Kategori, Merek, Pakaian, Pembeli
from .serializers import KategoriSerializer, MerekSerializer, PakaianSerializer, PembeliSerializer

class KategoriViewSet(viewsets.ModelViewSet):
    queryset = Kategori.objects.all()
    serializer_class = KategoriSerializer

class MerekViewSet(viewsets.ModelViewSet):
    queryset = Merek.objects.all()
    serializer_class = MerekSerializer

class PakaianViewSet(viewsets.ModelViewSet):
    queryset = Pakaian.objects.all()
    serializer_class = PakaianSerializer

class PembeliViewSet(viewsets.ModelViewSet):
    queryset = Pembeli.objects.all()
    serializer_class = PembeliSerializer


