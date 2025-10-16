import json
import os
from src.projects.models import Project

DATA_FILE = "data/projects.json"

def load_projects():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w') as f:
            json.dump([], f)
        return []

    with open(DATA_FILE, "r") as f:
        try:
            projects_data = json.load(f)
        except json.JSONDecodeError:
            return []
    return projects_data

def save_projects(projects):
    with open(DATA_FILE, "w") as f:
        json.dump(projects, f, indent=4)

def add_project(project):
    projects = load_projects()
    projects.append(project.to_dict())
    save_projects(projects)

def get_project(project_id):
    projects = load_projects()
    for project in projects:
        if project["id"] == project_id:
            return project
    return None

def add_collaborator(project_id, collaborator):
    projects = load_projects()
    for project in projects:
        if project["id"] == project_id:
            if collaborator not in project["collaborators"]:
                project["collaborators"].append(collaborator)
            break
    save_projects(projects)