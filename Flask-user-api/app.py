from flask import Flask, request, jsonify

app = Flask(__name__)

# User data list
users = [
    {"id": 1, "name": "Aman"},
    {"id": 2, "name": "Riya"}
]

# GET - Show all users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)


# POST - Add a new user
@app.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()

    new_user = {
        "id": len(users) + 1,
        "name": data["name"]
    }

    users.append(new_user)
    return jsonify(new_user)


# PUT - Update a user
@app.route("/users/<int:id>", methods=["PUT"])
def update_user(id):
    data = request.get_json()

    for user in users:
        if user["id"] == id:
            user["name"] = data["name"]
            return jsonify(user)

    return jsonify({"message": "User not found"})


# DELETE - Delete a user
@app.route("/users/<int:id>", methods=["DELETE"])
def delete_user(id):
    for user in users:
        if user["id"] == id:
            users.remove(user)
            return jsonify({"message": "User deleted"})

    return jsonify({"message": "User not found"})


if __name__ == "__main__":
    app.run(debug=True)