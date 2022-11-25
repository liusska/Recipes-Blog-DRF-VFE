from rest_framework import status
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .serializers import RecipeSerializer
from .models import Recipe


class LeadPagination(PageNumberPagination):
    page_size = 6


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all().order_by('-publication_date')
    serializer_class = RecipeSerializer
    pagination_class = LeadPagination
    permission_classes = [IsAuthenticatedOrReadOnly]
    search_fields = ['title', 'ingredients', 'category']
    filter_backends = (SearchFilter,)

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            instance = serializer.save(author=self.request.user)
            return instance


class UserRecipeView(APIView):
    def get(self, request):
        recipes = Recipe.objects.filter(author=self.request.user.id).order_by('-publication_date')
        serializer = RecipeSerializer(recipes, many=True)
        return Response(data=serializer.data,  status=status.HTTP_200_OK)
