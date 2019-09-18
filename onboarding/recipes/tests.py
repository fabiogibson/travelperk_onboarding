from utils.testing import *

from recipes.models import Recipe, Ingredient


class RecipeTestCase(ModelAPITestCase):
    MODEL = Recipe
    NESTED_MODELS = {'ingredients': Ingredient}
    __test__ = True

    def create_data(self):
        return {
            'name': 'test_recipe',
            'description': 'some description',
            'ingredients': [{
                'name': 'test_ingredient',
            }]
        }

    def update_data(self):
        return {
            'name': 'test_recipe',
            'description': 'some description',
            'ingredients': [{
                'name': 'test_ingredient',
            }]
        }


