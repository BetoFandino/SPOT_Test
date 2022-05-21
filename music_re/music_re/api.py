from rest_framework import routers

from catalog_api import views as catalog_views
from user_api import views as user_views

router = routers.DefaultRouter()
router.register(r'catalog', catalog_views.CatalogViewSet, basename="catalog")
router.register(r'create_user', user_views.UserViewSet, basename="create_user")

urlpatterns = router.urls
