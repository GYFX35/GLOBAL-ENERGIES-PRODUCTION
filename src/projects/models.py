import uuid

class Project:
    def __init__(self, name, description, owner, collaborators=None):
        self.id = str(uuid.uuid4())
        self.name = name
        self.description = description
        self.owner = owner
        self.collaborators = collaborators if collaborators is not None else []

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "owner": self.owner,
            "collaborators": self.collaborators
        }