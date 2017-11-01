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

    def register_user(self, username, email, password, cpassword):
        """This method will validate and verify the user details before storing"""
        regusername = "[a-zA-Z0-9- .]"
        regemail = r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        if re.match(regusername, username):
            if username != '' and email != '' and password != '' and cpassword.strip():
                if username not in users.keys():
                    if email not in users.keys():
                        if password == cpassword:
                            if re.search(regemail, email):
                                if len(password) >= 6:
                                    users[email] = {'uname': username,
                                                    'email': email,
                                                    'password': password,
                                                    }
                                    return "registration_success"
                                return "check_password_length"
                            return "check_email_pattern"
                        return "check_match_passwords"
                    return "check_email_existence"
                return "check_username_existence"
            return "check_null_fields"
        return "check_username_pattern"

    def user_login(self, email, password):
        """This will help the user log in and access the resources"""
        if email != '' and password != '' and email != '  ' and password != '  ':
            if email in users.keys():
                result = users[email]
                result_password = result['password']
                if result_password == password:

                    return "login_success"
                return "true"
            return "check_email_password_existence"
        return "check_null_empty_fields"

    def get_username(self, email):
        """ Get username from the email provided by the user"""
        if email in users.keys():
            res_user = users[email]
            return res_user['uname']
        return False

    def get_email(self, email):
        """Retrieve the email for the user already registered"""
        if email in users.keys():
            res_email = users[email]
            return res_email['email']
        return False
