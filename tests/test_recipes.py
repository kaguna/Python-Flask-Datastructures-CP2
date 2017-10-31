from unittest import TestCase
from classes.categories import Categories


class TestRecipes(TestCase):
    """This class will handle all the functions to test for the recipe name"""

    def setUp(self):
        """This method defines the test fixture for all test to be undertaken"""
        self.new_category = Categories()

        """
        This will test recipe name entry under all circumstances when creating a recipe.
        """
    def test_empty_recipename(self):
        """Test on the messge poped upon registering empty recipe name"""
        emptyfield = self.new_category.create_recipe(" ", "Lunch", "add description of recipe", "kaguna@gmail.com")
        self.assertEqual("null_empty_field", emptyfield, "Please give the recipe name.")

    def test_empty_procedure(self):
        """Test on the messge poped upon registering empty recipe procedure"""
        emptyfield = self.new_category.create_recipe("sembe", "Lunch", " ", "kaguna@gmail.com")
        self.assertEqual("null_empty_field", emptyfield, "Please give the recipe procedure.")

    def test_null_recipename(self):
        """Test if recipe name is null"""
        nullfield= self.new_category.create_recipe(" ", "Lunch", "add description of recipe", "kaguna@gmail.com" )
        self.assertEqual("null_empty_field", nullfield, "Please give the recipe name.")

    def test_pattern_recipename(self):
        """Test if pattern name follows the pattern given"""
        recnamepattern =  self.new_category.create_recipe("#^", "lunch", "add description of recipe","kaguna@gmail.com" )
        self.assertEqual("recipename_pattern", recnamepattern, "Invalid recipe name.")

    def test_recipename_exist(self):
        """Test if recipe name exists in the recipe list"""
        self.new_category.recipes = []
        self.new_category.create_recipe("sembe","lunch", "add description of recipe", "kaguna@gmail.com")
        recipenameexist = self.new_category.create_recipe("sembe","lunch", "add description of recipe", "kaguna@gmail.com")
        self.assertEqual("recipename_uniqueness", recipenameexist, "Recipe name exists.")

    def test_recipename_create(self):
        """Test if recipe name is different and register"""
        self.new_category.recipes = []
        self.new_category.create_recipe("Githeri","lunch", "add description of recipe", "kaguna@gmail.com")
        create_recname = self.new_category.create_recipe("ugali","supper", "add description of recipe", "kaguna@gmail.com")
        self.assertEqual("success", create_recname, "Recipe created successfully.")

        """
           This will test recipe name entry when updating a recipe.
           """

    # def test_update_pattern_recipename(self):
    #     """Test if new recipe name follows the pattern given"""
    #     recnamepattern = self.new_category.create_recipe("ugali", '@@###', "Lunch", "kaguna@gmail.com")
    #     self.assertEqual("recipename_pattern", recnamepattern, "Invalid new recipe name.")

    def test_update_recipename_exist(self):
        """Test if the new recipe name exists in the recipe list"""
        self.new_category.recipes = []
        self.new_category.create_recipe("ugali", "sembe", "Lunch", "kaguna@gmail.com")
        recipenameexist = self.new_category.create_recipe("ugali", "sembe", "Lunch", "kaguna@gmail.com")
        self.assertEqual("recipename_uniqueness", recipenameexist, "Recipe name exists.")

    def test_recipename_update(self):
        """Test if recipe name is unique and register"""
        self.new_category.recipes = []
        self.new_category.create_recipe("ugali", "Sembe", "Lunch", "kaguna@gmail.com")
        create_recname = self.new_category.create_recipe("ugali", "ngima", "Lunch", "kaguna@gmail.com")
        self.assertEqual("success", create_recname, "Recipe updated successfully.")


