from unittest import TestCase
from classes.recipes import Recipes


class TestRecipes(TestCase):
    """
    This class will handle all the functions to test for the recipe name"""

    def setUp(self):
        """This method defines the test fixture for all test to be undertaken"""
        self.new_recipe = Recipes()

    # This will test recipe name entry under all circumstances when creating a recipe.

    def test_empty_recipename(self):
        """Test on the messge poped upon registering empty recipe name"""
        emptyfield = self.new_recipe.create_recipe(" ", "Lunch", "add description of recipe", "kaguna@gmail.com")
        self.assertEqual("check_null_empty_field", emptyfield, "Please give the recipe name.")

    def test_empty_procedure(self):
        """Test on the messge poped upon registering empty recipe procedure"""
        emptyfield = self.new_recipe.create_recipe("sembe", "Lunch", " ", "kaguna@gmail.com")
        self.assertEqual("check_null_empty_field", emptyfield, "Please give the recipe procedure.")

    def test_null_recipename(self):
        """
        Test if recipe name is null
        """
        nullfield = self.new_recipe.create_recipe(" ", "Lunch", "add description of recipe",
                                                  "kaguna@gmail.com")
        self.assertEqual("check_null_empty_field", nullfield, "Please give the recipe name.")

    def test_invalid_recipename(self):
        """
        Test if pattern name follows the pattern given
        """
        invalidrecipename = self.new_recipe.create_recipe("#^", "lunch", "add description of recipe",
                                                          "kaguna@gmail.com")
        self.assertEqual("check_recipename_pattern", invalidrecipename, "Invalid recipe name.")

    def test_valid_recipename(self):
        """Test if recipe name is valid i.e. follows the pattern provided"""
        valid_recipename = self.new_recipe.create_recipe("Tea", "lunch", "add description of recipe",
                                                         "kaguna@gmail.com")
        self.assertEqual("check_register_recipe_success", valid_recipename, "Recipe successfully added.")

    def test_recipename_exist(self):
        """Test if recipe name exists in the recipe list"""
        self.new_recipe.recipes = []
        self.new_recipe.create_recipe("sembe", "lunch", "add description of recipe", "kaguna@gmail.com")
        recipenameexist = self.new_recipe.create_recipe("sembe", "lunch", "add description of recipe",
                                                        "kaguna@gmail.com")
        self.assertEqual("check_recipename_uniqueness", recipenameexist, "Recipe name exists.")

    def test_creation_of_recipename(self):
        """Test if recipe name is different and register"""
        self.new_recipe.recipes = []
        self.new_recipe.create_recipe("Githeri", "lunch", "add description of recipe", "kaguna@gmail.com")
        create_recipe = self.new_recipe.create_recipe("ugali", "supper", "add description of recipe",
                                                      "kaguna@gmail.com")
        self.assertEqual("check_register_recipe_success", create_recipe, "Recipe created successfully.")

    # Below functions will test recipe name entry when updating a recipe.

    def test_invalid_recipename_updte(self):
        """Test if pattern name follows the pattern given"""
        invalidrecipename = self.new_recipe.edit_recipe("ugali", "%%%^", "Lunch", "kaguna@gmail.com")
        self.assertEqual("check_invalid_recipename", invalidrecipename, "Invalid recipe name.")

    def test_empty_recipename_updte(self):
        """Test if recipe name is   empty"""
        emptyrecipename = self.new_recipe.edit_recipe("ugali", " ", "Lunch", "kaguna@gmail.com")
        self.assertEqual("check_null_empty_field", emptyrecipename, "Invalid recipe name.")
