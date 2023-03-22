from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models.todos_model import Todo

class User:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.todo_list = []

    @classmethod
    def get_one_user_with_todos(cls, data):
        query  = "SELECT * "
        query += "FROM users u "
        query += "LEFT JOIN todos t ON u.id = t.user_id "
        query += "WHERE u.id = %(id)s;"

        results = connectToMySQL(DATABASE).query_db(query, data)
        current_user = cls(results[0])

        for row in results:
            if row ["name"] != None:
                current_todo = {
                    "id" : row["t.id"],
                    "name" : row["name"],
                    "status" : row["status"],
                    "created_at" : row["t.created_at"],
                    "updated_at" : row["t.updated_at"],
                    "user_id" : row["user_id"]
                }
                current_todo_object = Todo(current_todo)
                current_user.todo_list.append(current_todo_object)
        print("Todos", current_user.todo_list)
        return current_user