# This file handles the routing processes and the redirection to the functions and other pages.
from flask import Flask, render_template, request, session, g
from classes.users import Users
from classes.categories import Categories
from classes.recipes import Recipes

import os
app = Flask(__name__)
from app import app
app.secret_key = os.urandom(24)
# Needed to keep the client sessions secure

newUser = Users()
# This is creating an instance of the class users
newCategory = Categories()
# This is creating an instance of the class Categories

newRecipes = Recipes()
# This is creating an instance of the class Categories



@app.route("/")
def index():
    """This method redirects the requests to the index file which is the landing page."""
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    This method accepts data from the registration form
    and redirects the data to the method that handles registration in the class users
    """

    if request.method == "POST":
        email = request.form['email']
        username = request.form['username']
        password = request.form['pass']
        confirm_password = request.form['cpass']
        registration_return_value = newUser.register_user(
            username, email, password, confirm_password)

        # The registration_return_value is a variable that holds the return values from the method
        # where registration takes place.

        if registration_return_value == "registration_success":
            # This condition checks whether the registration was successful
            # and redirects the user to the login page.

            session['username'] = username
            return_message = "Registration was successful."
            return render_template('login.html', message=return_message)

        elif registration_return_value == "check_null_fields":
            return_message = "Please fill in all the fields"
            return render_template("register.html", message=return_message)

        elif registration_return_value == "check_username_pattern":
            return_message = "Invalid username format."
            return render_template("register.html", message=return_message)

        elif registration_return_value == "check_password_length":
            return_message = "Password must have a minimum of 8 characters."
            return render_template("register.html", message=return_message)

        elif registration_return_value == "check_username_existence":
            return_message = "Username already exists."
            return render_template("register.html", message=return_message)
        elif registration_return_value == "match_passwords":
            return_message = "Passwords did not match."
            return render_template("register.html", message=return_message)

        elif registration_return_value == "check_email_pattern":
            return_message = "Invalid email format."
            return render_template("register.html", message=return_message)

        elif registration_return_value == "check_email_existence":
            return_message = "Email already exists"
            return render_template("register.html", message=return_message)
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    This method does the validation and verification of the users details and gives
    access to the resources using the sessions.
    """
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        login_return_value = newUser.user_login(email, password)
        if login_return_value == "login_success":
            username = newUser.get_username(email)
            email = newUser.get_email(email)
            session['user'] = username
            session['email'] = email
            list_categories = newCategory.view_category(session['email'])

            # After successful login process, the user is granted with the list of
            # categories and the email in session stored in the variable list_categories

            return render_template("dashboard.html", category_details=list_categories)

        elif login_return_value == "check_email_password_existence":
            return_message = "Wrong credentials given."
            return render_template("login.html", message=return_message)

        elif login_return_value == "check_null_empty_fields":
            return_message = "Please fill all fields"
            return render_template("login.html", message=return_message)
        else:
            return_message = "Invalid credentials, try again"
            return render_template("login.html", message=return_message)
    return render_template("login.html")


@app.route("/create_category", methods=["GET", "POST"])
def create_category():
    """
    This method accepts data from the create category form and routes
    it to the method in the category class.
    """
    if g.user:  # checks whether the user is ni session first
        if request.method == "POST":
            category_name = request.form['cat_name']
            category_owner = request.form['cat_owner']
            create_category = newCategory.create_category(
                category_name, category_owner)
            # The create_category gives the return string after creating a category

            list_categories = newCategory.view_category(category_owner)
            # The list_categories retrieves all the categories belonging to the user in session

            if create_category == "success":
                return_message = "Category created successfully"
                return render_template("dashboard.html", message=return_message,
                                       alerttype="success", category_details=list_categories)

            elif create_category == "null_empty_field":
                return_message = "Please input the category name of the field."
                return render_template("dashboard.html", message=return_message,
                                       alerttype="danger", category_details=list_categories)

            elif create_category == "catname_pattern":
                return_message = "Invalid category name format."
                return render_template("dashboard.html", message=return_message,
                                       alerttype="danger", category_details=list_categories)

            elif create_category == "catname_uniqueness":
                return_message = "Similar category name found."
                return render_template("dashboard.html", message=return_message,
                                       alerttype="danger", category_details=list_categories)

            else:
                return_message = "Error occured, try again later."
                return render_template("dashboard.html", message=return_message,
                                       alerttype="danger", category_details=list_categories)
        else:
            list_categories = newCategory.view_category(g.user)
        return render_template("dashboard.html", category_details=list_categories)
    return render_template("login.html")


@app.route('/recipes/<category>', methods=["POST", "GET"])
def recipes(category):
    """
    This method uses category name to route to the specific category's recipes
    """
    if g.user:
        list_recipes = newRecipes.view_recipes(category, g.user)
        # The variable list_recipes returns a list of the recipes belonging to the
        # user in session under a specific category name

        return render_template("recipes.html", category_details=category, recipe_details=list_recipes)
    return render_template("login.html")


@app.route('/create_recipe', methods=["POST", "GET"])
def create_recipe():
    """
    This method creates a recipe having acquired the recipe name, category owner and the category name
    """
    if g.user:
        if request.method == "POST":
            category_name = request.form['category_name']
            category_owner = request.form['cat_owner']
            recipe_name = request.form['recipe_name']
            recipe_procedure = request.form['procedure']

            create_recipe = newRecipes.create_recipe(
                recipe_name, category_name, recipe_procedure, category_owner)
            # The create recipe requires the above parameters to create the recipe from a specific category.

            list_recipes = newRecipes.view_recipes(category_name, g.user)
            if create_recipe == "register_recipe_success":
                msg_flag = "Recipe created successfully"
                return render_template("recipes.html", message=msg_flag, alerttype="success",
                                       recipe_details=list_recipes, category_details=category_name)

            elif create_recipe == "check_null_empty_field":
                msg_flag = "Please input the recipe name of the field."
                return render_template("recipes.html", message=msg_flag, alerttype="danger",
                                       recipe_details=list_recipes, category_details=category_name)

            elif create_recipe == "check_recipename_pattern":
                msg_flag = "Invalid recipe name format."
                return render_template("recipes.html", message=msg_flag, alerttype="danger",
                                       recipe_details=list_recipes, category_details=category_name)

            elif create_recipe == "check_recipename_uniqueness":
                msg_flag = "Similar Recipe name found."
                return render_template("recipes.html", message=msg_flag, alerttype="danger",
                                       recipe_details=list_recipes, category_details=category_name)

            else:
                msg_flag = "Error occured, try again later."
                return render_template("recipes.html", message=msg_flag, alerttype="danger",
                                       recipe_details=list_recipes, category_details=category_name)
    return render_template("login.html")


@app.route('/edit_category', methods=["POST", "GET"])
def edit_category():
    """
    This method helps in updating the category name.
    Old category name and the new category name are the major parameters for this method
    """
    if g.user:
        if request.method == "POST":
            category_name = request.form['category_name']
            current_name = request.form['current_category_name']
            category_owner = g.user
            list_categories = newCategory.view_category(category_owner)
            # The list_categories variable stores a list of categories belonging to the user in session.

            edit_category = newCategory.edit_category(
                current_name, category_name, category_owner)
            #
            if edit_category == "success":
                return_message = "Category name changed."
                return render_template("dashboard.html", message=return_message, alerttype="success",
                                       category_details=list_categories)
            elif edit_category == "null_empty_field":
                return_message = "Please input the the category name."
                return render_template("dashboard.html", message=return_message, alerttype="danger",
                                       category_details=list_categories)

            elif edit_category == "categoryname_pattern":
                return_message = "Invalid category name format."
                return render_template("dashboard.html", message=return_message, alerttype="danger",
                                       category_details=list_categories)

            elif edit_category == "categoryname_uniqueness":
                return_message = "Similar category name found."
                return render_template("dashboard.html", message=return_message, alerttype="danger",
                                       category_details=list_categories)

            else:
                return_message = "error"
                return render_template("dashboard.html", message=return_message, alerttype="error",
                                       category_details=list_categories)
   
    return render_template("login.html")


@app.route('/delete_category/<category_name>', methods=["POST", "GET"])
def delete_category(category_name):
    """
    This method handles the deletion of a specific category from among many categories
    """
    if g.user:
        delete_category = newCategory.delete_category(category_name, g.user)
        # The delete_category variable returns the remaining categories after deletion.
        return_message = "Category name deleted."
        return render_template("dashboard.html", message=return_message, alerttype="success",
                               category_details=delete_category)
    return render_template("login.html")


@app.route('/edit_recipe', methods=["POST", "GET"])
def edit_recipe():
    """Handles editing the recipe name"""
    if g.user:
        if request.method == "POST":
            category_name = request.form['category_name']
            new_recipe_name = request.form['new_recipe_name']
            current_recipe_name = request.form['current_recipe_name']
            list_recipes = newRecipes.view_recipes(category_name, g.user)
            edit_rec = newRecipes.edit_recipe(
                current_recipe_name, new_recipe_name, category_name, g.user)
            if edit_rec == "success":
                msg_flag = "Recipe name changed."
                return render_template("recipes.html", message=msg_flag, alerttype="success",
                                       recipe_details=list_recipes, category_details=category_name)
            elif edit_rec == "null_empty_field":
                msg_flag = "Please input the the category name."
                return render_template("recipes.html", message=msg_flag, alerttype="danger",
                                       recipe_details=list_recipes, category_details=category_name)

            elif edit_rec == "recipename_pattern":
                msg_flag = "Invalid recipe name format."
                return render_template("recipes.html", message=msg_flag, alerttype="danger",
                                       recipe_details=list_recipes, category_details=category_name)

            elif edit_rec == "recipename_uniqueness":
                msg_flag = "Similar recipe name found."
                return render_template("recipes.html", message=msg_flag, alerttype="danger",
                                       recipe_details=list_recipes, category_details=category_name)

            else:
                msg_flag = "error"
                return render_template("recipes.html", message=msg_flag, alerttype="error",
                                       recipe_details=list_recipes, category_details=category_name)
    return render_template("login.html")


@app.route('/delete_recipe', methods=["POST", "GET"])
def delete_recipe():
    """delete recipe"""
    if g.user:
        if request.method == "POST":
            category_name = request.form['category_name']
            recipe_name = request.form['recipe_name']
            delete_recipe = newRecipes.delete_recipe(
                recipe_name, category_name, g.user)
            msg_flag = "Recipe name deleted."
            list_recipes = newRecipes.view_recipes(category_name, g.user)
            return render_template("recipes.html", message=msg_flag, alerttype="success",
                                   recipe_details=delete_recipe, category_details=category_name)
        return render_template("recipes.html")
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
