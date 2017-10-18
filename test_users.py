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
        self.assertEqual("check_password_pattern", result, "User registration successful")

    def test_null_email_field(self):
        """ This will test whether the email field is null"""
        nullemailresult = self.new_user.register_user("kaguna", "", "password", "password")
        self.assertEqual("null_fields", nullemailresult, "Please fill the Email field.")


    def test_null_username_field(self):
        """ This will test whether the username field is null"""
        nullusernameresult = self.new_user.register_user("", "kaguna@gmail.com", "password", "password")
        self.assertEqual("check_username_pattern",nullusernameresult,"Please fill the Username field.")


    def test_null_password_field(self):
        """ This will test whether the password field is null"""
        nullpasswordresult = self.new_user.register_user("kaguna", "kaguna@gmail.com", "", "password")
        self.assertEqual("null_fields", nullpasswordresult, "Please fill the password field.")


    def test_null_cpassword_field(self):
        """ This will test whether the password field is null"""
        nullcpasswordresult = self.new_user.register_user("kaguna", "kaguna@gmail.com", "password", "")
        self.assertEqual("null_fields", nullcpasswordresult, "Please fill the confirm password field.")

    def test_empty_cpassword_field(self):
        """ This will test whether the password field is empty"""
        emptycpasswordresult = self.new_user.register_user("kaguna", "kaguna@gmail.com", "password", " ")
        self.assertEqual("null_fields", emptycpasswordresult, "Please fill the confirm password field.")




    def test_passwordEqualCpassword_field(self):
        """ This will test whether the password match the confirm password"""
        comparepasswordresult = self.new_user.register_user("kaguna", "kaguna@gmail.com", "password", "pass")
        self.assertEqual("match_passwords", comparepasswordresult, "The passwords given do not match.")



