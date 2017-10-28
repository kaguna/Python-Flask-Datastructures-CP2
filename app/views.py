from flask import Flask, render_template, request, session, g
from  classes.users import Users
from  classes.categories import Categories
import os
app = Flask(__name__)
from app import app

app.secret_key = os.urandom(24)
newUser = Users()
newCategory = Categories()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """ Handles registration process"""

    if request.method == "POST":
        email = request.form['email']
        username = request.form['username']
        password = request.form['pass']
        cpassword = request.form['cpass']
        regreturnvalue = newUser.register_user(username, email, password, cpassword)

        if regreturnvalue == "dict_success":
            session['username'] = username
            msg_flag = "Registration was successful."
            return render_template('login.html', message=msg_flag, )

        elif regreturnvalue == "null_fields":
            msg_flag = "Please fill in all the fields"
            return render_template("register.html", message=msg_flag)

        elif regreturnvalue == "check_username_pattern":
            msg_flag = "Invalid username format."
            return render_template("register.html", message=msg_flag)

        elif regreturnvalue == "check_password_pattern":
            msg_flag = "Password must have a minimum of 8 characters .i.e mixture of numbers and characters."
            return render_template("register.html", message=msg_flag)

        elif regreturnvalue == "username_in_dict":
            msg_flag = "Username already exists."
            return render_template("register.html", message=msg_flag)
        elif regreturnvalue == "match_passwords":
            msg_flag = "Passwords did not match."
            return render_template("register.html", message=msg_flag)

        elif regreturnvalue == "check_email_pattern":
            msg_flag = "Invalid email format."
            return render_template("register.html", message=msg_flag)

        elif regreturnvalue == "email_in_dict":
            msg_flag = "Email already exists"
            return render_template("register.html", message=msg_flag)
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Handles the login process"""
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        loginreturnvalue = newUser.user_login(email, password)
        if loginreturnvalue == "success":
            username = newUser.get_username(email)
            email = newUser.get_email(email)
            session['user'] = username
            session['email'] = email
            list_categories = newCategory.view_category(session['email'])
            return render_template("dashboard.html", cat_name=list_categories)

        elif loginreturnvalue == "check_email_password_dict":
            msg_flag = "Wrong credentials given."
            return render_template("login.html", message=msg_flag)

        elif loginreturnvalue == "check_email_password_dict":
            msg_flag = "Invalid credentials given."
            return render_template("login.html", message=msg_flag)
        elif loginreturnvalue == "null_empty_fields":
            msg_flag = "Please fill all fields"
            return render_template("login.html", message=msg_flag)
        else:
            msg_flag = "Invalid credentials, try again"
            return render_template("login.html", message=msg_flag)
    return render_template("login.html")


@app.route("/create_category", methods=["GET", "POST"])
def create_category():
    """Handles creation of yummy categories"""
    if g.user:
        if request.method == "POST":
            category_name = request.form['cat_name']
            category_owner = request.form['cat_owner']
            create_category = newCategory.create_category(category_name, category_owner)
            """This retrieves all the categories belonging to the user in session"""
            list_categories = newCategory.view_category(category_owner)
            if create_category == "success":
                msg_flag = "Category created successfully"
                return render_template("dashboard.html", message=msg_flag, alerttype="success", cat_name=list_categories)

            elif create_category == "null_empty_field":
                msg_flag = "Please input the category name of the field."
                return render_template("dashboard.html", message=msg_flag, alerttype="danger", cat_name=list_categories)

            elif create_category == "catname_pattern":
                msg_flag = "Invalid category name format."
                return render_template("dashboard.html", message=msg_flag, alerttype="danger", cat_name=list_categories)

            elif create_category == "catname_uniqueness":
                msg_flag = "Similar category name found."
                return render_template("dashboard.html", message=msg_flag, alerttype = "danger", cat_name=list_categories)

            else:
                msg_flag = "Error occured, try again later."
                return render_template("dashboard.html", message=msg_flag, alerttype="danger", cat_name=list_categories)
        else:
            list_categories = newCategory.view_category(g.user)
        return render_template("dashboard.html", cat_name=list_categories)
    return render_template("login.html")


@app.route('/recipes/<category>', methods=["POST", "GET"])
def recipes(category):
    if g.user:
        list_recipes = newCategory.view_recipes(category, g.user)
        return render_template("recipes.html", cat_name=category, recipe_name=list_recipes)
    return render_template("login.html")


@app.route('/create_recipe', methods=["POST", "GET"])
def create_recipe():
    """Handles creation of yummy specific category's recipes"""
    if g.user:
        if request.method == "POST":
            category_name = request.form['cat_name']
            category_owner = request.form['cat_owner']
            recipe_name = request.form['recipe_name']
            create_recipe = newCategory.create_recipe(recipe_name, category_name, category_owner)
            """This retrieves all the recipes belonging to the category and the user in session"""
            list_recipes = newCategory.view_recipes(category_name, g.user)
            if create_recipe == "success":
                msg_flag = "Recipe created successfully"
                return render_template("recipes.html", message=msg_flag, alerttype="success",
                                       recipe_name=list_recipes, cat_name=category_name)

            elif create_recipe == "null_empty_field":
                msg_flag = "Please input the recipe name of the field."
                return render_template("recipes.html", message=msg_flag, alerttype="danger",
                                       recipe_name=list_recipes, cat_name=category_name)

            elif create_recipe == "recipename_pattern":
                msg_flag = "Invalid recipe name format."
                return render_template("recipes.html", message=msg_flag, alerttype="danger",
                                       recipe_name=list_recipes, cat_name=category_name)

            elif create_recipe == "recipename_uniqueness":
                msg_flag = "Similar Recipe name found."
                return render_template("recipes.html", message=msg_flag, alerttype="danger",
                                       recipe_name=list_recipes, cat_name=category_name)

            else:
                msg_flag = "Error occured, try again later."
                return render_template("recipes.html", message=msg_flag, alerttype="danger",
                                       recipe_name=list_recipes, cat_name=category_name)
    return render_template("login.html")


@app.route('/edit_category', methods=["POST", "GET"])
def edit_category():
    """Handles editing the category name"""
    if g.user:
        if request.method == "POST":
            category_name = request.form['cat_name']
            current_name = request.form['current_cat_name']
            category_owner = g.user
            list_categories = newCategory.view_category(category_owner)
            edit_cat = newCategory.edit_category(current_name, category_name, category_owner)
            if edit_cat == "success":
                msg_flag = "Category name changed."
                return render_template("dashboard.html", message=msg_flag, alerttype="success",
                                       cat_name=list_categories)
            elif edit_cat == "null_empty_field":
                msg_flag = "Please input the the category name."
                return render_template("dashboard.html", message=msg_flag, alerttype="danger",
                                       cat_name=list_categories)

            elif edit_cat == "categoryname_pattern":
                msg_flag = "Invalid category name format."
                return render_template("dashboard.html", message=msg_flag, alerttype="danger",
                                       cat_name=list_categories)

            elif edit_cat == "categoryname_uniqueness":
                msg_flag = "Similar category name found."
                return render_template("dashboard.html", message=msg_flag, alerttype="danger",
                                       cat_name=list_categories)

            else:
                msg_flag = "error"
                return render_template("dashboard.html", message=msg_flag, alerttype="error",
                                       cat_name=list_categories)
    return render_template("login.html")


@app.route('/delete_category/<category_name>', methods=["POST", "GET"])
def delete_category(category_name):
    """delete category"""
    if g.user:
       delete_cat = newCategory.delete_category(category_name,g.user)
       msg_flag = "Category name deleted."
       return render_template("dashboard.html", message=msg_flag, alerttype="success",
                              cat_name=delete_cat)
    return render_template("login.html")


@app.route('/delete_recipe/<recipe_name>', methods = ["POST","GET"])
def delete_recipe(recipe_name):
    """delete recipe"""
    if g.user:
       delete_recip = newCategory.delete_recipe(recipe_name)
       msg_flag = "Recipe name deleted."
       return render_template("recipes.html", message=msg_flag, alerttype="success", recipe_name=delete_recip)
    return render_template("login.html")


@app.before_request
def before_request():
    g.user = None
    if 'email' in session:
        g.user = session['email']


@app.route('/logout')
def logout():
    """ method to logout a user"""
    session.pop('email', None)
    return render_template("login.html")
