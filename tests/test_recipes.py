from unittest import TestCase
from classes.categories import Categories


class TestRecipes(TestCase):
    """This class will handle all the functions to test for the recipe name"""

    def setUp(self):
        """This method defines the test fixture for all test to be undertaken"""
        self.new_category = Categories()

        """
        This will test recipe name entry under all circumstances.
        """
    def test_empty_recipename(self):
        """Test if recipe name is empty"""
        emptyfield = self.new_category.create_recipe(" ", "Lunch", "kaguna@gmail.com")
        self.assertEqual("null_empty_field", emptyfield, "Please give the recipe name.")

    def test_null_recipename(self):
        """Test if recipe name is null"""
        nullfield= self.new_category.create_recipe(" ", "Lunch", "kaguna@gmail.com" )
        self.assertEqual("null_empty_field", nullfield, "Please give the recipe name.")

    def test_pattern_recipename(self):
        """Test if pattern name follows the pattern given"""
        recnamepattern =  self.new_category.create_recipe("#^", "lunch","kaguna@gmail.com" )
        self.assertEqual("recipename_pattern", recnamepattern, "Invalid category name.")

    def test_recipename_exist(self):
        """Test if recipe name exists in the dictionary"""
        self.new_category.recipes = {}
        self.new_category.create_recipe("sembe","lunch", "kaguna@gmail.com")
        recipenameexist = self.new_category.create_recipe("sembe","lunch", "kaguna@gmail.com")
        self.assertEqual("recipename_uniqueness", recipenameexist, "Recipe name exists.")

    def test_recipename_create(self):
        """Test if recipe name is different and register"""
        self.new_category.recipes = {}
        self.new_category.create_recipe("Githeri","lunch", "kaguna@gmail.com")
        create_recname = self.new_category.create_recipe("ugali","supper", "kaguna@gmail.com")
        self.assertEqual("success", create_recname, "Recipe created successfully.")


