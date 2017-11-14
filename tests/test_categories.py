from unittest import TestCase
from classes.categories import Categories


class TestCategories(TestCase):
    """
    This class will handle all the functions to test for the category name
    """

    def setUp(self):
        """
        This method defines the test fixture for all test to be undertaken
        """
        self.new_category = Categories()

    def test_create_categoryname_pattern(self):
        """
        Test if category name follows the pattern given
        """
        categorynamepattern = self.new_category.create_category("#^", "kaguna@gmail.com")
        self.assertEqual("check_invalid_category_name", categorynamepattern, "Invalid category name.")

    def test_categoryname_existence(self):
        """
        Test if category name exists in the list
        """
        self.new_category.categories = []
        self.new_category.create_category("lunch", "kaguna@gmail.com")
        categoryname_exist = self.new_category.create_category("lunch", "kaguna@gmail.com")
        self.assertEqual("check_category_name_existence", categoryname_exist, "Category name exists.")

    def test_empty_categoryname(self):
        """
        Test if category name is null
        """
        emptycategoryname = self.new_category.create_category(" ", "kaguna@gmail.com")
        self.assertEqual("check_null_empty_field", emptycategoryname,
                         "Please fill the Categoryname field.")

    def test_successful_categoryname_creation(self):
        """
        Test if category name is different and register
        """
        self.new_category.categories = []
        self.new_category.create_category("lunch", "kaguna@gmail.com")
        create_categoryname = self.new_category.create_category("supper", "kagunaa@gmail.com")
        self.assertEqual("check_category_creation_success", create_categoryname,
                         "Category created successfully.")

    # Below methods will test when updating the category name

    def test_update_categoryname_pattern(self):
        """
        Test if category name follows the pattern given
        """
        category_name_pattern = self.new_category.edit_category("Luncho", "@@@", "karyorkir@gmail.com")
        self.assertEqual("check_invalid_category_name", category_name_pattern, "Invalid category name.")

    def test_update_empty_categoryname(self):
        """
        Test if category name is empty or null
        """
        empty_category_name = self.new_category.edit_category("Luncho", " ", "karyorkir@gmail.com")
        self.assertEqual("check_null_empty_field", empty_category_name, "Invalid category name.")

