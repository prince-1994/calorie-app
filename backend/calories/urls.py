from rest_framework import routers
from .views import FoodCalorieViewSet

router = routers.DefaultRouter()
router.register('food', FoodCalorieViewSet, basename='foodcalories')
urlpatterns = router.urls