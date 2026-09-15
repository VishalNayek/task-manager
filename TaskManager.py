##This Task Manager is created based on OOP Concepts

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



class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        next_id=0
        for task in self.tasks:
            next_id = max(next_id, task.id)
        task = Task(next_id+1, title, description)
        self.tasks.append(task)

    def view_tasks(self):
        if (self.tasks):
            for task in self.tasks:
                print(task)
        else:
            print("No tasks to print")

    def find_task(self,task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def delete_task(self, task_id):
        task = self.find_task(task_id)
        if task is not None:
            self.tasks.remove(task)
        else:
            print(f'No task found with id: {task_id} to delete.')

    def complete_task(self, task_id):
        task = self.find_task(task_id)
        if task is not None:
            task.complete()
        else:
            print(f'No task found with id: {task_id} to complete.')

    def edit_task(self, task_id, title, description):
        task = self.find_task(task_id)
        if task is not None:
            task.edit(title,description)
        else:
            print(f'No task found with id: {task_id} to edit.')

    def save_tasks(self):
        task_list = []
        for task in self.tasks:
            task_list.append(task.to_dict())
        with open("tasks.json", "w") as file:
            json.dump(task_list, file, indent=4)

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                task_list =  json.load(file)
                for task in task_list:
                    self.tasks.append(Task.from_dict(task))
        except FileNotFoundError:
            print("No file Found")
        except json.JSONDecodeError:
            print("Invalid JSON")


def main():
    manager = TaskManager()
    manager.load_tasks()

    while True:
        display_menu()
    
        choice = input("Enter a choice: ")
    
        if(choice == '1'):
            title = input("Enter Title: ")
            description = input("Enter Description: ")
            manager.add_task(title,description)

        elif(choice =='2'):
            manager.view_tasks()      

        elif(choice=='3'):
            try:
                task_id = int(input("Enter the id of the task: "))
                title = input("Enter Title: ")
                description = input("Enter Description: ")
                manager.edit_task(task_id, title, description)
            except ValueError:
                print("Id should be an integer")

        elif(choice=='4'):
            try:
                task_id = int(input("Enter the id of the task: "))
                manager.complete_task(task_id)
            except ValueError:
                print("Id should be an integer")

        elif(choice=='5'):
            try:
                task_id = int(input("Enter the id of the task: "))
                manager.delete_task(task_id)
            except ValueError:
                print("Id should be an integer")

        elif(choice=='6'):
            manager.save_tasks()
            print('Exited Task Manager.')
            break
        
        else:
            print('Invalid Choice')

def display_menu():
    print("====================")
    print("TASK MANAGER")
    print("====================")
    print("1. Create Task")
    print("2. View Tasks")
    print("3. Edit Task")
    print("4. Complete Task")
    print("5. Delete Task")
    print("6. Exit Task Manager")

main()