from rest_framework import serializers
from .models import Recipe
from account.models import User


class RecipeSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(
        source='author.username'
    )

    class Meta:
        model = Recipe
        fields = '__all__'

    def validate(self, data):
        data['author'] = self.context['request'].user
        print(self.context['request'].user)
        return data
