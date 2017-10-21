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
