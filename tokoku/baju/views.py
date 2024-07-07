from rest_framework import viewsets
from .models import Kategori, Merek, Pakaian
from .serializers import KategoriSerializer, MerekSerializer, PakaianSerializer

class KategoriViewSet(viewsets.ModelViewSet):
    queryset = Kategori.objects.all()
    serializer_class = KategoriSerializer

class MerekViewSet(viewsets.ModelViewSet):
    queryset = Merek.objects.all()
    serializer_class = MerekSerializer

class PakaianViewSet(viewsets.ModelViewSet):
    queryset = Pakaian.objects.all()
    serializer_class = PakaianSerializer

