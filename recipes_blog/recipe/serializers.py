from rest_framework import serializers
from .models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(
        source='author.username'
    )

    class Meta:
        model = Recipe
        fields = '__all__'

    def validate(self, data):
        print(data)
        data['author'] = self.context['request'].user
        print(self.context['request'].user)
        return data
