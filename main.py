import json

def main():
    tasks = load_tasks()
    while True:
        display_menu()

        choice = input("Enter a choice: ")

        if(choice == '1'):
            create_tasks(tasks)
        elif(choice =='2'):
            view_tasks(tasks)
        elif(choice=='3'):
            edit_tasks(tasks)
        elif(choice=='4'):
            complete_task(tasks)
        elif(choice=='5'):
            delete_tasks(tasks)
        elif(choice=='6'):
            exit_app(tasks)
            print('Exited Task Manager.')
            break
        else:
            print('Invalid Choice')

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []

def exit_app(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)
    print("Tasks saved successfully!")


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


def create_tasks(tasks):
    highest_id = 0
    if(tasks):
        for task in tasks:
            if(task['id']> highest_id):
                highest_id = task['id']

    title = input("Enter the title of the task: ")
    description = input("Enter the description of the task: ")
    new_task = {
        "id": highest_id+1,
        "title": title,
        "description": description,
        "completed": False
    }
    tasks.append(new_task)
    print("Task created successfully!")


def view_tasks(tasks):
    if(tasks):
        for task in tasks:
            if(task['completed'] == False):
                status = 'Pending'
            else:
                status = 'Completed'
            print(f"ID: {task['id']}, Title: {task['title']}, Description: {task['description']}, Status: {status}")
    else:
        print('No tasks available.')

def edit_tasks(tasks):
    if(tasks):
        try:
            inputId = int(input("Enter the Id of the task you want to edit: "))
            task = find_task(tasks, inputId)
            if task is not None:
                task['title'] = input("Enter the new title: ")
                task['description'] = input("Enter the new description: ")
            else:
                print(f"No task found with id {inputId}")
        except ValueError:
            print("Please enter an integer.")
    else:
        print("No tasks to edit.")

def complete_task(tasks):
        if(tasks):
            try:
                inputId = int(input("Enter the Id of the task you want to complete: "))
                task = find_task(tasks, inputId)
                if task is not None:
                    if(task['completed'] == True):
                        print("Task has already been completed")
                    else:
                        task['completed'] = True
                        print("Task has been completed.")
                else:
                    print(f"No task found with id {inputId}")
            except ValueError:
                print("Please enter an integer.")
        else:
            print("No tasks present to complete.")


def delete_tasks(tasks):
    if(tasks):
            try:
                inputId = int(input("Enter the Id of the task you want to delete: "))
                task = find_task(tasks, inputId)
                if task is not None:
                    tasks.remove(task)
                    print("Task has been deleted.")
                else:
                    print(f"No task found with id {inputId}")
            except ValueError:
                print("Please enter an integer.")
    else:
        print("No tasks to delete.")

def find_task(tasks, inputId):
    for task in tasks:
        if(task['id'] == inputId):
            return task
    return None

main()