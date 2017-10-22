import re


class Categories(object):
    """
    this class will handle all the functions related to the users
    """
    categories = {}
    recipes = {}

    def __init__(self, category_name=None, category_owner=None):
        """constructor to initialize the global variables"""

        self.category_name = category_name
        self.category_owner = category_owner

    def create_category(self, category_name, category_owner):

        regexcategory_name = "[a-zA-Z0-9- .]"

        if re.match(regexcategory_name, category_name):

            if category_name != '' and category_name.strip():

                if category_name not in self.categories.keys():

                        self.categories[category_name] = {'cat_name': category_name,
                                                          'cat_owner': category_owner,
                                                          }
                        return "success"
                return "catname_uniqueness"
            return "null_empty_field"
        return "catname_pattern"

    def view_category(self, category_owner):
        cats = self.categories
        my_category = []
        for category in cats:
            if cats[category]['cat_owner'] == category_owner:
               my_category.append(category)
        return my_category

    def create_recipe(self, recipe_name, category_name, category_owner):

     regexrecipe_name = "[a-zA-Z0-9- .]"

     if re.match(regexrecipe_name, recipe_name):

         if recipe_name != '' and recipe_name.strip():

             if recipe_name not in self.recipes.keys():

                     self.recipes[recipe_name] = {'recipe_name': recipe_name,
                                                  'cat_name': category_name,
                                                  'cat_owner': category_owner,
                                                  }
                     return "success"
             return "recipename_uniqueness"
         return "null_empty_field"
     return "recipename_pattern"


    def view_recipes(self, category_name):
        data = self.recipes
        my_recipes = []
        for recipe in data:
            if data[recipe]['cat_name'] == category_name:
               my_recipes.append(recipe)
        return my_recipes