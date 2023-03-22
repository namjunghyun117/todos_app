
from flask_app import app
from flask_app.controllers import todos_controller, users_controller

# At the very end don't forget to place the "run" command
if __name__ == "__main__":
    app.run(debug = True)

