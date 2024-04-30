from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework import routers
from django.urls import path, include
from search.views import HeritageLostObjectDocumentView


router = routers.DefaultRouter(trailing_slash=False)

router.register(r'heritage_lost_objects-search', HeritageLostObjectDocumentView)

urlpatterns = router.urls

