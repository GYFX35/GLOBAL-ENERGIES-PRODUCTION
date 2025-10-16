import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from flask import Flask, request, jsonify, send_from_directory
from src.projects.models import Project
from src.projects.db import load_projects, add_project, get_project, add_collaborator

app = Flask(__name__, static_folder=os.path.abspath('src/frontend'))

@app.route("/projects", methods=["POST"])
def create_project():
    data = request.get_json()
    if not data or "name" not in data or "owner" not in data:
        return jsonify({"error": "Missing project name or owner"}), 400

    project = Project(
        name=data["name"],
        description=data.get("description", ""),
        owner=data["owner"]
    )
    add_project(project)
    return jsonify(project.to_dict()), 201

@app.route("/projects", methods=["GET"])
def list_projects():
    projects = load_projects()
    return jsonify(projects)

@app.route("/projects/<project_id>", methods=["GET"])
def view_project(project_id):
    project = get_project(project_id)
    if project:
        return jsonify(project)
    return jsonify({"error": "Project not found"}), 404

@app.route("/projects/<project_id>/collaborators", methods=["POST"])
def add_project_collaborator(project_id):
    data = request.get_json()
    if not data or "collaborator" not in data:
        return jsonify({"error": "Missing collaborator"}), 400

    project = get_project(project_id)
    if not project:
        return jsonify({"error": "Project not found"}), 404

    add_collaborator(project_id, data["collaborator"])
    return jsonify({"message": "Collaborator added successfully"})

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == "__main__":
    app.run(debug=True)