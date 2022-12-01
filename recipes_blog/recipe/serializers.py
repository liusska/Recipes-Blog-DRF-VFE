from rest_framework import serializers
from .models import Recipe, Rate


class RecipeSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(
        source='author.username'
    )

    class Meta:
        model = Recipe
        fields = '__all__'


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = ('user', 'recipe', 'rate')

