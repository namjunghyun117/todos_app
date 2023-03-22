
from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.users_model import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route("/user/<int:id>", methods=["GET"])
def get_user_by_id(id):
    if "user_id" not in session:
        return redirect("/")
    else:
    # Grab the id, place it in a dictionary
        data = {
            "id" : id
        }
        # Send the dictionary to the query in our model
        current_user = User.get_one_user_with_todos(data)
        # The response from the model send it to the template
        return render_template("/user.html", current_user=current_user)

@app.route("/", methods=["GET"])
@app.route("/login", methods=["GET"])
@app.route("/registration", methods=["GET"])
def get_login_registration():
    return render_template("login_reg.html")

@app.route("/user/new", methods=["POST"])
def create_user():
    if User.validate_registration(request.form) == True:
        encrypted_password = User.encrypt_password(request.form["password"], bcrypt)
        new_user = {
            **request.form,
            "password" : encrypted_password
        }
        user_id = User.create_one(new_user)
        session["full_name"] = f"{request.form['first_name']} {request.form['last_name']}"
        session["user_id"] = user_id
        return redirect("/todos")
    else:
        print("There is an error!")
        return redirect("/")
    
@app.route("/login", methods=["POST"])
def user_login():
    login_user = {
        "email" : request.form["email_login"]
    }
    current_user = User.get_one(login_user)
    if current_user != None:
        if User.validate_password(request.form["password_login"], current_user.password, bcrypt) == True:
            session["full_name"] = f"{current_user.first_name} {current_user.last_name}"
            session["user_id"] = current_user.id
            return redirect("/todos")
        else:
            return redirect("/")
    else:
        return redirect("/")

@app.route("/logout", methods=["POST"])
def user_logout():
    del session["user_id"]
    del session["full_name"]
    return redirect("/")

# @app.route("/logout", methods=["POST"])
# def user_logout():
#     session.clear()
#     return redirect('/')
