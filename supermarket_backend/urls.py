from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import SimpleRouter
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from supermarket_backend.apps.inventory.views import (
    ItemViewSet,
)

from supermarket_backend.apps.transaction.views import (
    BillViewSet,
)

router = SimpleRouter()
router.register("items", ItemViewSet, basename="items")
router.register("bills", BillViewSet, basename="bills")
urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/accounts/auth/", include("dj_rest_auth.urls")),
    path("api/accounts/auth/register", include("dj_rest_auth.registration.urls")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path("", include(router.urls)),
]
