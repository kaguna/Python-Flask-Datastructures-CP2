# This file will run the tests for the user credentials provided in the form
from unittest import TestCase
from classes.users import Users


class TestUsers(TestCase):
    """This class will handle all the functions to test for the user entry functions"""

    def setUp(self):
        """This method defines the test fixture for all test to be undertaken"""
        self.new_user = Users()

    # This will test all the registration credentials under all circumstances.

    def test_register_user(self):
        """Test registration when all inputs are stored in the dictionary."""
        result = self.new_user.register_user("kaguna", "kagunaa@gmail.com", "qwerty123", "qwerty123")
        self.assertEqual("registration_success", result, "User registration successful")

    def test_null_email_field(self):
        """ This will test whether the email field is null"""
        nullemailresult = self.new_user.register_user("kaguna", "", "password", "password")
        self.assertEqual("check_null_fields", nullemailresult, "Please fill the Email field.")


    def test_invalid_email(self):
        """ This will test whether the email has . symbol"""
        emailpattern = self.new_user.register_user("kaguna", "kaguna@gmailcom", "password", "password")
        self.assertEqual("check_email_pattern", emailpattern, "Invalid email format.")

    def test_null_username_field(self):
        """ This will test whether the username field is null"""
        nullusernameresult = self.new_user.register_user("", "kaguna@gmail.com", "password", "password")
        self.assertEqual("check_username_pattern", nullusernameresult, "Please fill the Username field.")

    def test_null_password_field(self):
        """ This will test whether the password field is null"""
        nullpasswordresult = self.new_user.register_user("kaguna", "kaguna@gmail.com", "", "password")
        self.assertEqual("check_null_fields", nullpasswordresult, "Please fill the password field.")

    def test_null_cpassword_field(self):
        """ This will test whether the password field is null"""
        nullcpasswordresult = self.new_user.register_user("kaguna", "kaguna@gmail.com", "password", "")
        self.assertEqual("check_null_fields", nullcpasswordresult, "Please fill the confirm password field.")

    def test_empty_cofirm_password_field(self):
        """ This will test whether the password field is empty"""
        emptycpasswordresult = self.new_user.register_user("kaguna", "kaguna@gmail.com", "password", " ")
        self.assertEqual("check_null_fields", emptycpasswordresult, "Please fill the confirm password field.")

    def test_passwordEqualCofirmpassword_field(self):
        """ This will test whether the password match the confirm password"""
        comparepasswordresult = self.new_user.register_user("kaguna", "kaguuna@gmail.com", "qwerty123", "jimmy987")
        self.assertEqual("check_match_passwords", comparepasswordresult, "The passwords given do not match.")

    # This will test the login credentials under all given conditions.

    def test_login_success(self):
        """ Test the inputs required for a valid login"""
        self.new_user.users = {}
        self.new_user.register_user("kaguna", "kaguna@gmail.com", "password123", "password123")
        valid_login= self.new_user.user_login("kaguna@gmail.com", "password123")
        self.assertEqual("check_password_existence", valid_login, "Login successful.")

    def test_login_match_password(self):
        """ Test login when the password differs with the one in the dictionary.."""
        self.new_user.users = {}
        self.new_user.register_user("kaguna", "kaguna@gmail.com", "password", "password")
        invalidmatchpassword = self.new_user.user_login("kaguna@gmail.com", "pass")
        self.assertEqual("check_password_existence", invalidmatchpassword, "Incorrect password given.")

    def test_login_match_email(self):
        """ Test login when the email differs with the one in the dictionary."""
        self.new_user.users = {}
        self.new_user.register_user("kaguna", "kaguna@gmail.com", "password", "password")
        invalidmatchpassword = self.new_user.user_login("jimmy@gmail.com", "password")
        self.assertEqual("check_email_password_existence", invalidmatchpassword, "Incorrect password given.")

    def test_login_inputnull(self):
        """ Test login when all inputs are null"""
        nullinputs = self.new_user.user_login("", "")
        self.assertEqual("check_null_empty_fields", nullinputs, "Please fill all the fields.")

    def test_login_nullemail(self):
        """ Test login when email input is null"""
        nullemail = self.new_user.user_login("", "password")
        self.assertEqual("check_null_empty_fields", nullemail, "Please fill the email field.")

    def test_login_nullpassword(self):
        """ Test login when password input is null"""
        nullpassword = self.new_user.user_login("kaguna@gmail.com", "")
        self.assertEqual("check_null_empty_fields", nullpassword, "Please fill the password field.")

    def test_login_emptypassword(self):
        """ Test login when password input is empty"""
        emptypassword = self.new_user.user_login("kaguna@gmail.com", "  ")
        self.assertEqual("check_null_empty_fields", emptypassword, "Password field should not be empty.")

    def test_login_emptyemail(self):
        """ Test login when password input is empty"""
        emptyemail = self.new_user.user_login("  ", "password")
        self.assertEqual("check_null_empty_fields", emptyemail, "Email field should not be empty.")
