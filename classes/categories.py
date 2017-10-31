import re


class Categories(object):
    """
    this class will handle all the functions related to the categories and recipes
    """
    categories = []
    recipes = []

    def __init__(self, category_name=None, category_owner=None):
        """constructor to initialize the global variables"""

        self.category_name = category_name
        self.category_owner = category_owner

    def create_category(self, category_name, category_owner):
        """This will create new and unique category"""
        personal_categories = [owner_list for owner_list in self.categories
                               if category_owner in owner_list]

        similar_cat_list = [searched_cat_name for searched_cat_name in personal_categories
                            if searched_cat_name[0] == category_name]

        regexcategory_name = "[a-zA-Z0-9- .]"

        category_name = category_name.replace(" ","_")
        if re.match(regexcategory_name, category_name):

            if category_name != '' and category_name.strip():
                if self.categories != []:
                    if similar_cat_list == []:
                        self.categories.append([category_name, category_owner, ])
                        return "success"
                    return "catname_uniqueness"
                self.categories.append([category_name, category_owner, ])
                return "success"
            return "null_empty_field"
        return "catname_pattern"

    def view_category(self, category_owner):
        """This will display the categories"""
        personal_list = [owner_list for owner_list in self.categories if category_owner in owner_list]
        return personal_list

    def edit_category(self, current_name, new_name, category_owner):
        """Update the category name"""
        personal_categories = [owner_list for owner_list in self.categories
                               if category_owner in owner_list]

        similar_cat_list = [searched_cat_name for searched_cat_name in personal_categories
                            if searched_cat_name[0] == new_name]
        regexcategory_name = "[a-zA-Z0-9- .]"
        if re.match(regexcategory_name, new_name):
            if new_name != '' and new_name.strip():
                for catList in personal_categories:
                    if current_name in catList:
                        if similar_cat_list == []:
                            category_name_index = personal_categories.index(catList)
                            personal_categories[category_name_index][0] = new_name
                            """Update the category name in the recipes list"""
                            for recList in self.recipes:
                                if current_name in recList:
                                    for index in range(0, len(self.recipes)):
                                        """loop all the indexes with the current"""
                                        self.recipes[index][1] = new_name
                                    return "success"

                            return "success"
                        return "categoryname_uniqueness"
            return "null_empty_field"
        return "categoryname_pattern"

    def delete_category(self, category_name, category_owner):
        """This will delete the categories from user in session"""
        personal_categories = [owner_list for owner_list in self.categories
                               if category_owner in owner_list]

        specific_category_recipes = [recipes for recipes in self.recipes
                                     if category_owner == recipes[2] and category_name == recipes[1]]
        """delete recipes for the deleted category"""
        for recList in self.recipes:
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

    def create_recipe(self, recipe_name, category_name, category_owner):
        """This will add a recipe to the list"""
        specific_category_recipes = [recipes for recipes in self.recipes
                               if category_name in recipes]

        similar_recipe_list = [searched_recipe_name for searched_recipe_name in specific_category_recipes
                            if searched_recipe_name[0] == recipe_name]

        regexrecipe_name = "[a-zA-Z0-9- .]"

        if re.match(regexrecipe_name, recipe_name):

            if recipe_name != '' and recipe_name.strip():
                if self.recipes != []:
                    if similar_recipe_list == []:
                        self.recipes.append([recipe_name, category_name, category_owner,])
                        return "success"
                    return "recipename_uniqueness"
                self.recipes.append([recipe_name,category_name, category_owner])
                return "success"
            return "null_empty_field"
        return "recipename_pattern"

    def view_recipes(self, category_name, recipe_owner):
        """Displays the specific category's recipes"""
        specific_category_recipes = [recipes for recipes in self.recipes
                                     if recipe_owner == recipes[2] and category_name == recipes[1]]
        return specific_category_recipes

    def edit_recipe(self, current_recipe_name, new_recipe_name, category_name, recipe_owner):
        """Update the category name"""
        specific_category_recipes = [recipes for recipes in self.recipes
                                     if recipe_owner == recipes[2] and category_name == recipes[1]]

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
        """This will delete the recipes"""
        specific_category_recipes = [recipes for recipes in self.recipes
                                     if recipe_owner == recipes[2] and category_name == recipes[1]]
        for recList in specific_category_recipes:
            if recipe_name in recList:
                recipe_list_index = specific_category_recipes.index(recList)
                del self.recipes[recipe_list_index]
                del specific_category_recipes[recipe_list_index]
        return specific_category_recipes