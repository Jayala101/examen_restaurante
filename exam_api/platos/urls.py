# catalog/urls.py
from rest_framework.routers import DefaultRouter
from platos.views.platos import PlatosViewSet

router = DefaultRouter()
router.register(r'platos', PlatosViewSet, basename='platos')

urlpatterns = router.urls
