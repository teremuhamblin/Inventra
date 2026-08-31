from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from inventory.api.endpoints import CategoryViewSet, PartViewSet, StockItemViewSet

router = DefaultRouter()
router.register("categories", CategoryViewSet)
router.register("parts", PartViewSet)
router.register("stock", StockItemViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
