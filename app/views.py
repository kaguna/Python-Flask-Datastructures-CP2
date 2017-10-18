from flask import Flask, render_template, request, session
from users import Users
import os
app = Flask(__name__)
app.secret_key = os.urandom(24)
newUser = Users()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods = ["GET","POST"])
def register():
    """ Handles registration process"""

    if request.method == "POST":
        email = request.form['email']
        username = request.form['username']
        password = request.form['pass']
        cpassword = request.form['cpass']
        returnvalue = newUser.register_user(username, email, password, cpassword)

        if returnvalue == "dict_success":
            session['username'] = username
            msg_flag = "Registration was successful."
            return render_template('login.html', message=msg_flag)

        elif returnvalue == "null_fields":
            msg_flag = "Please fill in all the fields"
            return render_template("register.html", message=msg_flag)

        elif returnvalue == "check_username_pattern":
            msg_flag = "Invalid username format."
            return render_template("register.html", message=msg_flag)

        elif returnvalue == "check_password_pattern":
            msg_flag = "Password must have a minimum of 8 characters .i.e mixture of numbers and characters."
            return render_template("register.html", message=msg_flag)

        elif returnvalue == "username_in_dict":
            msg_flag = "Username already exists."
            return render_template("register.html", message=msg_flag)
        elif returnvalue == "match_passwords":
            msg_flag = "Passwords did not match."
            return render_template("register.html", message=msg_flag)


        elif returnvalue == "check_email_pattern":
            msg_flag = "Invalid email format."
            return render_template("register.html", message=msg_flag)


        elif returnvalue == "email_in_dict":
            msg_flag = "Email already exists"
            return render_template("register.html", message=msg_flag)
    return render_template("register.html")


@app.route("/login")
def login():

    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)
