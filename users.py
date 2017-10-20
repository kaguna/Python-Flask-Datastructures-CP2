import re
users = {}


class Users(object):
    """
    this class will handle all the functions related to the users
    """

    def __init__(self, username=None, email=None, password=None):
        """constructor to initialize the global variables"""

        self.username = username
        self.email = email
        self.password = password

    def register_user(self, username, email, password, cpassword):

        regusername = "[a-zA-Z0-9- .]"
        regemail = r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        regpassword = r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"

        if re.match(regusername, username):

            if username != '' and email != '' and password != '' and cpassword != '' and cpassword != ' ':

                if username not in users.keys():

                    if email not in users.keys():

                        if password == cpassword:

                            if re.search(regemail, email):

                                if re.search(regpassword, password):

                                    users[email] = {'uname': username,
                                                    'email': email,
                                                    'password': password,
                                                    }
                                    return "dict_success"
                                return "check_password_pattern"
                            return "check_email_pattern"
                        return "match_passwords"
                    return "email_in_dict"
                return "username_in_dict"
            return "null_fields"
        return "check_username_pattern"

    def user_login(self, email, password):
        """This will help the user log in and access the resources"""
        if email != '' and password != '' and email != '  ' and password != '  ':
            if email in users.keys():
                result = users[email]
                result_password = result['password']
                if result_password == password:

                    return "success"
                return "true"
            return "check_email_password_dict"
        return "null_empty_fields"

    def get_username(self, email):
        """ Get username from the email provided by the user"""
        if email in users.keys():
            res_user = users[email]
            return res_user['uname']
        return False

    def get_email(self, email):
        """Get the email from the dictionary"""
        if email in users.keys():
            res_email = users[email]
            return res_email['email']
        return False