from rest_framework.routers import DefaultRouter

from .views import AirportViewSet, FlightViewSet

router = DefaultRouter()
router.register(r'airport', AirportViewSet, basename='airport')
router.register(r'flight', FlightViewSet, basename='flight')
urlpatterns = router.urls
