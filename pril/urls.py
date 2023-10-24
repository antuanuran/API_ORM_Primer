from django.urls import include, path
from rest_framework.routers import DefaultRouter

from pril.views import import_data, show_catalog, show_product, postman, PhoneViewSet

router = DefaultRouter()
router.register("phones", PhoneViewSet)

urlpatterns = [
    path("products-import-data/", import_data),
    path("show_catalog/", show_catalog),
    path("show_catalog/<item>/", show_product),
    path("postman/", postman),
    path("", include(router.urls)),
]