from django.urls import path
from rest_framework import routers
from .views import RecipeViewSet, UserRecipeView
from comments.views import CommentViewSet

router = routers.DefaultRouter()
router.register('', RecipeViewSet)
router.register('', CommentViewSet)

urlpatterns = [
    path('user/', UserRecipeView.as_view()),

]

urlpatterns += router.urls