import re
import random
categories = {}
rangenumbers = range(1,100)
category_id= random.choice(rangenumbers)

class Categories(object):
    """
    this class will handle all the functions related to the users
    """

    def __init__(self, category_id=None, category_name=None, category_owner=None):
        """constructor to initialize the global variables"""

        self.category_id = category_id
        self.category_name = category_name
        self.category_owner = category_owner

    def create_category(self, category_id, category_name, category_owner):

        regexcategory_name = "[a-zA-Z0-9- .]"

        if re.match(regexcategory_name, category_name):

            if category_name != '' and category_name != ' ':

                if category_name not in categories.keys():

                    if category_id not in categories.keys():
                        categories[category_id] = {'cat_id': category_id,
                                     'cat_name': category_name,
                                      'cat_owner': category_owner,
                                    }
                        return "success"
                return "catid_unique"
            return "null_empty_field"
        return "catname_pattern"