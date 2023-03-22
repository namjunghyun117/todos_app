
from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.users_model import User

@app.route("/user/<int:id>", methods=["GET"])
def get_user_by_id(id):
    # Grab the id, place it in a dictionary
    data = {
        "id" : id
    }
    # Send the dictionary to the query in our model
    current_user = User.get_one_user_with_todos(data)
    # The response from the model send it to the template
    return render_template("/user.html", current_user=current_user)