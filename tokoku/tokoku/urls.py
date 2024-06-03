from django.urls import path, include
from rest_framework import routers
from baju.views import CategoryViewSet, ProductViewSet

router = routers.DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('products', ProductViewSet)

urlpatterns = [
    path('api', include(router.urls)),
]
