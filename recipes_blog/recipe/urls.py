from django.urls import path
from rest_framework import routers
from .views import RecipeViewSet, UserRecipeView

router = routers.DefaultRouter()
router.register('', RecipeViewSet)

urlpatterns = [
    path('user/', UserRecipeView.as_view()),
]
urlpatterns += router.urls