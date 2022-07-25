class Recipe:
    """Represents a Recipe."""
    def __init__(self, name: str, cooking_lvl: int, cooking_time: int, ingredients: list, recipe_type: str, description: str = None):
        self._set_name(name)
        self._set_cooking_lvl(cooking_lvl)
        self._set_cooking_time(cooking_time)
        self._set_ingredients(ingredients)
        self._set_recipe_type(recipe_type)
        self._set_description(description)

    def _set_name(self, name):
        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError("Error: Name not a string.")

    def _set_cooking_lvl(self, cooking_lvl):
        if isinstance(cooking_lvl, int):
            self.cooking_lvl = cooking_lvl
        else:
            raise ValueError("Error: Cooking level not a number.")

    def _set_cooking_time(self, cooking_time):
        if isinstance(cooking_time, int):
            self.cooking_time = cooking_time
        else:
            raise ValueError("Error: Cooking time not a number.")

    def _set_ingredients(self, ingredients):
        if isinstance(ingredients, list):
            self.ingredients = ingredients
        else:
            raise ValueError("Error: Ingredient not a list.")

    def _set_description(self, description):
        if description is None:
            self.description = None
            return
        if isinstance(description, str):
            self.description = description
        else:
            raise ValueError("Error: Description not a string.")
    
    def _set_recipe_type(self, recipe_type):
        valid_types = ["starter", "lunch", "dessert"]
        if recipe_type not in valid_types:
            raise ValueError("Error: Recipe type not a valid string.")
        elif isinstance(recipe_type, str):
            self.recipe_type = recipe_type
        else:
            raise ValueError("Error: Recipe type not a string.")

    def __str__(self):
        """Returns a string representation of the class."""

        return f"Name: {self.name}, " + \
                f"Cooking level: {self.cooking_lvl}, " + \
                f"Cooking time: {self.cooking_time}, " + \
                f"Ingredients: {self.ingredients}, " + \
                f"Description: {self.description}, " + \
                f"Recipe type: {self.recipe_type}"
