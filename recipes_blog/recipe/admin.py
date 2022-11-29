from django.contrib import admin
from .models import Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'likes_count']
    list_filter = ['publication_date']

    def likes_count(self, object):
        return object.like_set.count()