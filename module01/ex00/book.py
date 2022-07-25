import time
from datetime import datetime
from collections import Counter
from itertools import chain
from recipe import Recipe


class Book:
    """Represents a book containing Recipes."""
    def __init__(self, name: str):
        self._set_name(name)
        self.creation_date = datetime.now()
        self.last_update = self.creation_date
        self.recipes_list = {"starter": [], "lunch": [], "dessert": []}

    def _set_name(self, name):
        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError("Error: Name not a string.")

    def get_recipe_by_name(self, name):
        """Prints a recipe with the name \texttt{name} and returns the instance."""
        recipes = self.recipes_list.values()
        recipes = list(chain(*recipes))
        recipe = filter(lambda r: r.name == name, recipes)
        recipe = list(recipe)[0]
        print(str(recipe))
        return recipe

    def get_recipes_by_type(self, recipe_type):
        """Get all recipe names for a given recipe_type"""
        return self.recipes_list[recipe_type]

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if not isinstance(recipe, Recipe):
            raise ValueError("Error: recipe not a Recipe.")

        recipe_type = recipe.recipe_type
        self.recipes_list[recipe_type].append(recipe)
        self.last_update.fromtimestamp(time.time())
