import json

from task import Task

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        next_id=0
        for task in self.tasks:
            next_id = max(next_id, task.id)
        task = Task(next_id+1, title, description)
        self.tasks.append(task)
        return task

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
