from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from drf_writable_nested import WritableNestedModelSerializer

from recipes import models


class IngredientSerializer(serializers.ModelSerializer):

    """Ingredient model serializer."""

    class Meta:
        model = models.Ingredient
        fields = ('name', )


class RecipeSerializer(WritableNestedModelSerializer):

    """Recipe model serializer."""

    name = serializers.CharField(
        validators=[
            UniqueValidator(queryset=models.Recipe.objects.all())
        ]
    )

    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = models.Recipe
        fields = ('id', 'name', 'description', 'ingredients', )


