class Task:
    def  __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description
        self.completed = False

    def complete(self):
        self.completed = True

    def edit(self, title, description):
        self.title = title
        self.description = description


task = Task(1, 'Learn OOP', 'Practice OOP')
print(task.id)
print(task.title)
print(task.description)

task.edit('Learn AI', 'Practice AI')
print(task.id)
print(task.title)
print(task.description)
print(task.completed)