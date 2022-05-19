from rest_framework import routers

from catalog_api import views as catalog_views

router = routers.DefaultRouter()
router.register(r'catalog', catalog_views.CatalogViewSet, basename="catalog")

urlpatterns = router.urls
