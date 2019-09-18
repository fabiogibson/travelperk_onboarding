from rest_framework import routers

from recipes.views import RecipeView, IngredientView


router = routers.SimpleRouter()
router.register('recipe', RecipeView)
