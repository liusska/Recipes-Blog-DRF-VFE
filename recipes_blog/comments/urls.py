from django.urls import path
from rest_framework import routers

from comments.views import CommentRecipeViewSet

router = routers.DefaultRouter()
router.register('<int:pk>', CommentRecipeViewSet)

urlpatterns = router.urls