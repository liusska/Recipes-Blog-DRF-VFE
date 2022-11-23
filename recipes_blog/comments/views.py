from rest_framework import viewsets
from .serializers import CommentSerializer
from recipe.models import Recipe


class CommentRecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all().order_by('-publication_date')
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            comment = serializer.save(user=self.request.user)
            return comment