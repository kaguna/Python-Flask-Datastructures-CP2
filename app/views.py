from flask import Flask, render_template, request, session
import random
from users import Users
from categories import Categories
import os
app = Flask(__name__)
app.secret_key = os.urandom(24)
rangenumbers = range(1,100)
categoryId= random.choice(rangenumbers)
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
            return render_template('login.html', message=msg_flag)

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
            return render_template("dashboard.html")

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
    if request.method == "POST":
        category_name = request.form['cat_name']
        category_owner = request.form['cat_owner']
        category_id = categoryId
        create_category = newCategory.create_category(category_id, category_name, category_owner)
        if create_category == "success":
            msg_flag = "Category created successfully"
            return render_template("dashboard.html",message = msg_flag, alert = "success")

        elif create_category == "catid_uniqueness":
            msg_flag = "The category name already exists."
            return render_template("dashboard.html", message=msg_flag, alert = "danger")

        elif create_category == "null_empty_field":
            msg_flag = "Please input the category name of the field."
            return render_template("dashboard.html", message=msg_flag, alert = "danger")

        elif create_category == "catname_pattern":
            msg_flag = "Invalid category name format."
            return render_template("dashboard.html", message=msg_flag, alert = "danger")

        else:
            msg_flag = "Error occured, try again later."
            return render_template("dashboard.html", message=msg_flag , alert = "danger")


    return render_template("dashboard.html")




if __name__ == "__main__":
    app.run(debug=True)
