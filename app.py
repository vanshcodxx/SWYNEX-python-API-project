
from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = {}
next_id = 1


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "SWYNEX Python REST API is running",
        "endpoints": {
            "GET": "/tasks",
            "POST": "/tasks",
            "GET_ONE": "/tasks/<id>",
            "PUT": "/tasks/<id>",
            "DELETE": "/tasks/<id>"
        }
    }), 200


@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(list(tasks.values())), 200


@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = tasks.get(task_id)

    if task is None:
        return jsonify({"error": "Task not found"}), 404

    return jsonify(task), 200


@app.route("/tasks", methods=["POST"])
def create_task():
    global next_id

    if not request.is_json:
        return jsonify({"error": "Request must contain JSON"}), 400

    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON object"}), 400

    title = data.get("title")

    if not isinstance(title, str) or not title.strip():
        return jsonify({
            "error": "Title must be a non-empty string"
        }), 400

    task = {
        "id": next_id,
        "title": title.strip(),
        "completed": False
    }

    tasks[next_id] = task
    next_id += 1

    return jsonify(task), 201


@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = tasks.get(task_id)

    if task is None:
        return jsonify({"error": "Task not found"}), 404

    if not request.is_json:
        return jsonify({"error": "Request must contain JSON"}), 400

    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON object"}), 400

    if "title" in data:
        title = data["title"]

        if not isinstance(title, str) or not title.strip():
            return jsonify({
                "error": "Title must be a non-empty string"
            }), 400

        task["title"] = title.strip()

    if "completed" in data:
        if not isinstance(data["completed"], bool):
            return jsonify({
                "error": "Completed must be true or false"
            }), 400

        task["completed"] = data["completed"]

    return jsonify(task), 200


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    if task_id not in tasks:
        return jsonify({"error": "Task not found"}), 404

    deleted_task = tasks.pop(task_id)

    return jsonify({
        "message": "Task deleted successfully",
        "task": deleted_task
    }), 200


@app.errorhandler(404)
def page_not_found(error):
    return jsonify({"error": "Endpoint not found"}), 404


@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({"error": "HTTP method not allowed"}), 405


if __name__ == "__main__":
    app.run(debug=True)
