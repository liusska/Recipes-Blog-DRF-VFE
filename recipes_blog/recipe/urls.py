from django.urls import path
from rest_framework import routers
from .views import RecipeViewSet, LikeRecipeView, RateRecipeView

from comments.views import CommentViewSet

router = routers.DefaultRouter()
router.register('', RecipeViewSet)
router.register('', CommentViewSet)


urlpatterns = [
    path('likes/<int:pk>', LikeRecipeView.as_view()),
    path('rate/<int:pk>', RateRecipeView.as_view()),
]

urlpatterns += router.urls