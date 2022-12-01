from django.db import models
from django.core.validators import MinLengthValidator
from account.models import User


class Recipe(models.Model):
    TITLE_MAX_LENGTH = 150
    TITLE_MIN_LENGTH = 1
    TIME_MAX_LENGTH = 10
    TIME_MIN_LENGTH = 1
    DESCRIPTION_MIN_LENGTH = 1

    CATEGORY_CHOICE_OTHERS = 'Others'
    CATEGORY_CHOICE_SOUP = 'Soup'
    CATEGORY_CHOICE_DESSERT = 'Dessert'
    CATEGORY_CHOICE_SNACK = 'Snack'
    CATEGORY_CHOICE_SALAD = 'Salad'
    CATEGORY_CHOICE_BAKED = 'Baked'
    CATEGORY_CHOICE_MAIN = 'Main'
    CATEGORY_CHOICE_PIZZA = 'Pizza'

    CATEGORY_LIST = [(x, x) for x in (
        CATEGORY_CHOICE_SOUP,
        CATEGORY_CHOICE_DESSERT,
        CATEGORY_CHOICE_SNACK,
        CATEGORY_CHOICE_SALAD,
        CATEGORY_CHOICE_BAKED,
        CATEGORY_CHOICE_MAIN,
        CATEGORY_CHOICE_PIZZA,
        CATEGORY_CHOICE_OTHERS,
    )]

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
        blank=False,
        null=False,
        validators=(
            MinLengthValidator(TITLE_MIN_LENGTH),
        ),
    )

    category = models.CharField(
        max_length=max(len(x) for (x, _) in CATEGORY_LIST),
        default=CATEGORY_CHOICE_OTHERS,
        choices=CATEGORY_LIST,
        null=False,
        blank=False,
    )
    photo = models.ImageField(
        upload_to='recipes',
        null=True,
        blank=True,
    )
    video = models.URLField(
        blank=True,
        null=True
    )

    ingredients = models.TextField()
    description = models.TextField(
        validators=(
            MinLengthValidator(DESCRIPTION_MIN_LENGTH),
        )
    )

    time_in_minutes = models.CharField(
        max_length=TIME_MAX_LENGTH,
        blank=False,
        null=False,
        validators=(
            MinLengthValidator(TIME_MIN_LENGTH),
        ),
    )

    publication_date = models.DateTimeField(
        auto_now_add=True,
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    @property
    def get_average_rating(self):
        rate_count = self.rate_set.count()
        if rate_count == 0:
            return 0
        return sum(e.rate for e in self.rate_set.all()) / rate_count

    def __str__(self):
        return f'Title: {self.title}, Category {self.category}'


class Like(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )


class Rate(models.Model):
    RATE_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    ]

    rate = models.PositiveIntegerField(
        default=0,
        choices=RATE_CHOICES,
    )

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.recipe} - {self.user} Rate: {self.rate}'
