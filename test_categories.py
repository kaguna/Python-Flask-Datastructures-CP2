from unittest import TestCase
from categories import Categories


class TestCategories(TestCase):
    """This class will handle all the functions to test for the category name"""

    def setUp(self):
        """This method defines the test fixture for all test to be undertaken"""
        self.new_category = Categories()

        """
        This will test category name entry under all circumstances.
        """
    def test_empty_categoryname(self):
        """Test if category name is empty"""
        emptyfield = self.new_category.create_category(" ", "kaguna@gmail.com")
        self.assertEqual("null_empty_field", emptyfield, "Please give the category name.")

    def test_null_categoryname(self):
        """Test if category name is null"""
        nullfield =  self.new_category.create_category(" " ,"kaguna@gmail.com" )
        self.assertEqual("null_empty_field", nullfield, "Please give the category name.")

    def test_pattern_categoryname(self):
        """Test if category name follows the pattern given"""
        catnamepattern =  self.new_category.create_category("#^" ,"kaguna@gmail.com" )
        self.assertEqual("catname_pattern", catnamepattern, "Invalid category name.")

    def test_categoryname_exist(self):
        """Test if category name exists in the dictionary"""
        self.new_category.categories = {}
        self.new_category.create_category("lunch", "kaguna@gmail.com")
        catnameexist = self.new_category.create_category("lunch", "kaguna@gmail.com")
        self.assertEqual("catname_uniqueness", catnameexist, "Category name exists.")






