from unittest import TestCase
from users import Users


class TestUsers(TestCase):
    """This class will handle all the functions to test for the user entry functions"""

    def setUp(self):
        """This method defines the test fixture for all test to be undertaken"""
        self.new_user = Users()

    def test_register_user(self):
        """This will the function user_register"""
        result = self.new_user.register_user("kaguna", "kaguna@gmail.com", "password", "password")
        self.assertEqual(2, result, "User registration successful")

    def test_empty_email_field(self):
        """ This will test whether the email field is empty"""
        emptyemailresult = self.new_user.register_user("kaguna", " ", "password", "password")
        self.assertEqual(7, emptyemailresult, "Please fill the Email field.")


    def test_empty_username_field(self):
        """ This will test whether the username field is empty"""
        emptyusernameresult = self.new_user.register_user(" ", "kaguna@gmail.com", "password", "password")
        self.assertEqual(7,emptyusernameresult,"Please fill the Username field.")


    def test_empty_password_field(self):
        """ This will test whether the password field is empty"""
        emptypasswordresult = self.new_user.register_user("kaguna", "kaguna@gmail.com", " ", "password")
        self.assertEqual(7, emptypasswordresult, "Please fill the password field.")


    def test_empty_cpassword_field(self):
        """ This will test whether the password field is empty"""
        emptycpasswordresult = self.new_user.register_user("kaguna", "kaguna@gmail.com", "password", " ")
        self.assertEqual(7, emptycpasswordresult, "Please fill the confirm password field.")


    def test_passwordEqualCpassword_field(self):
        """ This will test whether the password field is empty"""
        comparepasswordresult = self.new_user.register_user("kaguna", "kaguna@gmail.com", "password", "pass")
        self.assertEqual(4, comparepasswordresult, "The passwords given do not match.")



