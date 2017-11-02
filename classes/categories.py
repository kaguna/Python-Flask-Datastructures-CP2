# This file handles the class for the categories and the CRUD methods associated to the categories
import re
from classes.recipes import Recipes


class Categories(object):
    """This class will handle all the functions related to the categories and recipes"""
    categories = []

    def __init__(self, category_name=None, recipe_name=None):
        """constructor to initialize the global variables"""

        self.category_name = category_name
        self.recipe_name = recipe_name
        self.newRecipe = Recipes()

    def create_category(self, category_name, category_owner):
        """This will create new and unique category"""
        personal_categories = [owner_list for owner_list in self.categories
                               if category_owner in owner_list]
        # The personal_categories variable hold several categories associated with the user in session.
        # In the case above i am using the list comprehension to retrieve the categories.

        similar_category_names = [searched_cat_name for searched_cat_name in personal_categories
                                  if searched_cat_name[0] == category_name]
        # The similar_category_names checks whether there exists a similar category name to the one
        # provided by the user.
        # In the case above i am using the list comprehension.

        regexcategory_name = "[a-zA-Z0-9- .]"

        if re.match(regexcategory_name, category_name):

            if category_name != '' and category_name != ' ' and category_name.strip():
                if self.categories != []:
                    if similar_category_names == []:
                        # If no such name registration takes place.

                        self.categories.append([category_name, category_owner, ])
                        return "success"
                    return "catname_uniqueness"
                self.categories.append([category_name, category_owner, ])
                return "success"
            return "null_empty_field"
        return "catname_pattern"

    def view_category(self, category_owner):
        """This will display the categories for the user in session"""
        personal_categories = [owner_list for owner_list in self.categories if category_owner in owner_list]
        # personal_categories holds several categories belonging to the owner who has logged in using
        # using list comprehensions.
        return personal_categories

    def edit_category(self, current_name, new_name, category_owner):
        """This method will aid in updating the category name"""
        personal_categories = [owner_list for owner_list in self.categories
                               if category_owner in owner_list]

        similar_category_name = [searched_cat_name for searched_cat_name in personal_categories
                                 if searched_cat_name[0] == new_name]
        regexcategory_name = "[a-zA-Z0-9- .]"
        if re.match(regexcategory_name, new_name):
            if new_name != '' and new_name.strip():
                for catList in personal_categories:
                    if current_name in catList:
                        if similar_category_name == []:
                            category_name_index = personal_categories.index(catList)
                            personal_categories[category_name_index][0] = new_name
                            # Update the category name in the recipes list
                            for recList in self.newRecipe.recipes:
                                if current_name in recList:
                                    for index in range(0, len(self.newRecipe.recipes)):
                                        # loop all the indexes with the current
                                        self.newRecipe.recipes[index][1] = new_name
                                        return "success"
                                return "category_name_not_found"
                        return "categoryname_uniqueness"
            return "null_empty_field"
        return "categoryname_pattern"

    def delete_category(self, category_name, category_owner):
        """
        This will help in  deleting the categories from user in session by providing the
        category name and the and the owner of the category.
            """
        personal_categories = [owner_list for owner_list in self.categories
                               if category_owner in owner_list]

        specific_category_recipes = [recipes for recipes in self.newRecipe.recipes
                                     if category_owner == recipes[2] and category_name == recipes[1]]
        # Using list comprehensions retrieve all the recipes for a specific category"""
        for recList in self.newRecipe.recipes:
            if category_name in recList:
                for index in range(0, len(specific_category_recipes)):
                    """loop all the indexes with the recipes of the specific category"""
                    del specific_category_recipes[index]

        for catList in personal_categories:
            if category_name in catList:
                category_list_index = personal_categories.index(catList)
                del self.categories[category_list_index]
                del personal_categories[category_list_index]
        return personal_categories
