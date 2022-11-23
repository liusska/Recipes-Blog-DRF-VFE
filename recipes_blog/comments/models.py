from django.db import models
from recipe.models import Recipe
from account.models import User
from django.core.validators import MinLengthValidator


class Comment(models.Model):
    COMMENT_MIN_LENGTH = 1
    COMMENT_MAX_LENGTH = 500

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    publication_date = models.DateTimeField(
        auto_now_add=True,
    )

    comment = models.TextField(
        max_length=COMMENT_MAX_LENGTH,
        validators=(
            MinLengthValidator(COMMENT_MIN_LENGTH),
        )
    )

    def __str__(self):
        return f'comment: {self.comment}, User {self.user}'