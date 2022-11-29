import os
from rest_framework import status
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .serializers import RecipeSerializer
from .models import Recipe, Like


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


class LikeBookView(APIView):
    def post(self, request, *args, **kwargs):
        recipe = Recipe.objects.get(pk=self.kwargs['pk'])
        like_object_by_user = recipe.like_set.filter(user=self.request.user.id).first()
        if like_object_by_user:
            like_object_by_user.delete()
        else:
            like = Like(
                recipe=recipe,
                user=self.request.user,
            )
            like.save()
        return Response(status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        recipe = Recipe.objects.get(pk=self.kwargs['pk'])
        recipe.likes_count = recipe.like_set.count()
        is_liked_by_user = recipe.like_set.filter(user_id=self.request.user.id).exists()
        return Response(
            data={
                "likes_count": recipe.likes_count,
                'is_liked': is_liked_by_user,
            },
            status=status.HTTP_201_CREATED
        )
