from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import KategoriViewSet, MerekViewSet, PakaianViewSet, PembeliViewSet

router = DefaultRouter()
router.register(r'kategori', KategoriViewSet)
router.register(r'merek', MerekViewSet)
router.register(r'pakaian', PakaianViewSet)
router.register(r'Pembeli', PembeliViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
