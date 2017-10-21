import re, random
class Categories(object):
    """
    this class will handle all the functions related to the users
    """
    categories = {}

    def __init__(self,category_name=None, category_owner=None):
        """constructor to initialize the global variables"""

        self.category_name = category_name
        self.category_owner = category_owner

    def create_category(self, category_name, category_owner):

        regexcategory_name = "[a-zA-Z0-9- .]"
        categoryId = random.choice(range(1, 100))

        if re.match(regexcategory_name, category_name):

            if category_name != '' and category_name != ' ':

                if category_name not in self.categories.keys():

                    if categoryId not in self.categories.keys():
                        self.categories[category_name] = {'cat_id': categoryId,
                                                    'cat_name': category_name,
                                                    'cat_owner': category_owner,
                                                    }
                        return "success"
                    return "catid_uniqueness"
                return "catname_uniqueness"
            return "null_empty_field"
        return "catname_pattern"



