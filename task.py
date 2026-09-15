import json

class Task:
    def  __init__(self, id, title, description, completed=False):
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed

    def complete(self):
        self.completed = True

    def edit(self, title, description):
        self.title = title
        self.description = description

    def __str__(self):
        return f"Id : {self.id}, Title : {self.title}, Description: {self.description}, Completed: {self.completed}."

    def to_dict(self):
        return {"id" : self.id, "title" : self.title, "description" : self.description, "completed" : self.completed}

    @classmethod
    def from_dict(cls,data):
        id = data['id']
        title = data['title']
        description = data['description']
        completed = data['completed']

        return cls(id, title, description, completed)