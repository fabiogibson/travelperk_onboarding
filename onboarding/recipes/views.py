from rest_framework import viewsets
from django.shortcuts import render

from recipes.models import Recipe, Ingredient
from recipes.serializers import RecipeSerializer, IngredientSerializer


class RecipeView(viewsets.ModelViewSet):
    """
    recipe api view
    """
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all().order_by('name')


class IngredientView(viewsets.ModelViewSet):
    """
    ingredient api view
    """
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all().order_by('name')
