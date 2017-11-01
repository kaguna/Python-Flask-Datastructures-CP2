from unittest import TestCase
from classes.categories import Categories


class TestCategories(TestCase):
    """This class will handle all the functions to test for the category name"""

    def setUp(self):
        """This method defines the test fixture for all test to be undertaken"""
        self.new_category = Categories()

    def test_pattern_categoryname(self):
        """Test if category name follows the pattern given"""
        catnamepattern = self.new_category.create_category("#^", "kaguna@gmail.com")
        self.assertEqual("catname_pattern", catnamepattern, "Invalid category name.")

    def test_categoryname_exist(self):
        """Test if category name exists in the list"""
        self.new_category.categories = []
        self.new_category.create_category("lunch", "kaguna@gmail.com")
        catnameexist = self.new_category.create_category("lunch", "kaguna@gmail.com")
        self.assertEqual("catname_uniqueness", catnameexist, "Category name exists.")

    def test_categoryname_create(self):
        """Test if category name is different and register"""
        self.new_category.categories = []
        self.new_category.create_category("lunch", "kaguna@gmail.com")
        create_catname = self.new_category.create_category("supper", "kagunaa@gmail.com")
        self.assertEqual("success", create_catname, "Category created successfully.")
