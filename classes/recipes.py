# This file handles the class for the recipes and the CRUD methods associated to the recipes
import re


class Recipes(object):
    """This class will handle all the functions related to the categories and recipes"""
    recipes = []

    def __init__(self,recipe_name=None, recipe_procedure=None):
        """constructor to initialize the global variables"""

        self.recipe_name = recipe_name
        self.recipe_procedure = recipe_procedure

    def create_recipe(self, recipe_name, category_name, recipe_procedure, category_owner):
        """This will add a recipe and the procedure for a specific category"""
        specific_category_recipes = [recipes for recipes in self.recipes
                                     if category_name in recipes]

        similar_recipe_name = [searched_recipe_name for searched_recipe_name in specific_category_recipes
                               if searched_recipe_name[0] == recipe_name]
        # using list comprehensions check whether the recipe name provided exists.

        regexrecipe_name = "[a-zA-Z0-9- .]"

        if re.match(regexrecipe_name, recipe_name):

            if recipe_name != '' and recipe_name.strip() and recipe_procedure.strip():
                if self.recipes != []:
                    if similar_recipe_name == []:
                        self.recipes.append([recipe_name, category_name, recipe_procedure, category_owner, ])
                        return "register_recipe_success"
                    return "check_recipename_uniqueness"
                self.recipes.append([recipe_name, category_name, recipe_procedure, category_owner, ])
                return "register_recipe_success"
            return "check_null_empty_field"
        return "check_recipename_pattern"

    def view_recipes(self, category_name, recipe_owner):
        """Displays the specific category's recipes"""
        specific_category_recipes = [recipes for recipes in self.recipes
                                     if recipe_owner == recipes[3] and category_name == recipes[1]]
        return specific_category_recipes

    def edit_recipe(self, current_recipe_name, new_recipe_name, category_name, recipe_owner):
        """This method will aid in the updating the category name"""
        specific_category_recipes = [recipes for recipes in self.recipes
                                     if recipe_owner == recipes[3] and category_name == recipes[1]]

        similar_recipe_list = [searched_recipe_name for searched_recipe_name in specific_category_recipes
                               if searched_recipe_name[0] == new_recipe_name]

        regexrecipe_name = "[a-zA-Z0-9- .]"
        if re.match(regexrecipe_name, new_recipe_name):
            if new_recipe_name != '' and new_recipe_name.strip():
                for recList in specific_category_recipes:
                    if current_recipe_name in recList:
                        if similar_recipe_list == []:
                            recipe_name_index = specific_category_recipes.index(recList)
                            specific_category_recipes[recipe_name_index][0] = new_recipe_name
                            return "success"
                        return "recipename_uniqueness"
            return "null_empty_field"
        return "recipename_pattern"

    def delete_recipe(self, recipe_name, category_name, recipe_owner):
        """This method will help in deleting deleting the recipes details"""
        specific_category_recipes = [recipes for recipes in self.recipes
                                     if recipe_owner == recipes[3] and category_name == recipes[1]]
        for recList in specific_category_recipes:
            if recipe_name in recList:
                recipe_list_index = specific_category_recipes.index(recList)
                del self.recipes[recipe_list_index]
                del specific_category_recipes[recipe_list_index]
        return specific_category_recipes
