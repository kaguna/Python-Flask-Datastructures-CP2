import re
users = {}

class Users(object):
    """
    this class will handle all the functions related to the users
    """

    def __init__(self, username=None, email=None, password=None):
        """constructor to initialize the global variables"""

        self.username=username
        self.email=email
        self.password=password

    def register_user(self, username, email, password, cpassword):

        regUsername = "[a-zA-Z0-9- .]"
        regEmail = r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        regPassword = r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"

        if re.match(regUsername,username):
            if username !=' ' and email !=' ' and password !=' ':
                if username not in users.keys():
                    if email not in users.keys():
                        if password == cpassword:
                            if re.search(regEmail, email):
                                if re.search(regPassword, password):
                                    users[email]={'uname':username, 'email':email, 'password':password}
                                    return 1
                                return 2
                            return 3
                        return 4
                    return 5
                return 6
            return 7
        return 8



