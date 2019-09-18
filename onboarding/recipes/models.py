from django.db import models

class Recipe(models.Model):

    """Recipe. """

    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Ingredient(models.Model):

    """Ingredient. """

    name = models.CharField(max_length=30)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                               related_name='ingredients')

    def __str__(self):
        return self.name
