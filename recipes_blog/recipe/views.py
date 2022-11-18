from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import RecipeSerializer
from .models import Recipe


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all().order_by('-publication_date')
    serializer_class = RecipeSerializer
    # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # serializer.save(author=self.request.user)
        if self.request.user.is_authenticated:
            instance = serializer.save(author=self.request.user)
            print(self.request.user)
            return instance
        else:
            print("user is NOT AUTHENTICATED!!!!!!!!!!!!!!!!!")
