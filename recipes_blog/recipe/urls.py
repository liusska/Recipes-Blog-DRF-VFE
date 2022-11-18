from rest_framework import routers
from .views import RecipeViewSet

router = routers.DefaultRouter()
router.register('', RecipeViewSet)

urlpatterns = router.urls