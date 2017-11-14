# This file will registration and retrieval of the users details
import re
users = {}


class Users(object):
    """This class will handle all the functions related to the users"""

    def __init__(self, username=None, email=None, password=None):
        """constructor to initialize the global variables"""
        self.username = username
        self.email = email
        self.password = password

    def register_user(self, username, email, password, confirm_password):
        """
        This method will validate and verify the user details before storing
        """
        nonspace_username = re.sub(r'\s+', ' ', username).strip()
        regusername = "[a-zA-Z0-9- .]"
        regemail = r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        if re.match(regusername, nonspace_username):
            if nonspace_username != '' and nonspace_username != ' ' and email != '' and password != '' \
                    and confirm_password.strip():
                if email not in users.keys():
                    if password == confirm_password:
                        if re.search(regemail, email):
                            if len(password) >= 8:
                                users[email] = {'username': nonspace_username,
                                                    'email': email,
                                                    'password': password,
                                                    }
                                return "registration_success"
                            return "check_password_length"
                        return "check_email_pattern"
                    return "check_match_passwords"
                return "check_email_existence"
            return "check_null_fields"
        return "check_username_pattern"

    def user_login(self, email, password):
        """This will help the user log in and access the resources"""
        if not (email and password):
            return "check_null_empty_fields"

        if email not in users.keys():
            return "check_email_password_existence"

        result_email = users[email]
        result_password = result_email['password']

        if result_password == password:
            return "login_success"
        else:
            return "check_password_existence"

    def get_username(self, email):
        """ Get username from the email provided by the user"""
        if email in users.keys():
            user_key_email = users[email]
            return user_key_email['username']
        return False

    def get_email(self, email):
        """Retrieve the email for the user already registered"""
        if email in users.keys():
            user_key_email = users[email]
            return user_key_email['email']
        return False
