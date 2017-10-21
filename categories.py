import re


class Categories(object):
    """
    this class will handle all the functions related to the users
    """
    categories = {}

    def __init__(self, category_name=None, category_owner=None):
        """constructor to initialize the global variables"""

        self.category_name = category_name
        self.category_owner = category_owner

    def create_category(self, category_name, category_owner):

        regexcategory_name = "[a-zA-Z0-9- .]"

        if re.match(regexcategory_name, category_name):

            if category_name != '' and category_name.strip():

                if category_name not in self.categories.keys():

                        self.categories[category_name] = {'cat_name': category_name,
                                                          'cat_owner': category_owner,
                                                          }
                        return "success"
                return "catname_uniqueness"
            return "null_empty_field"
        return "catname_pattern"