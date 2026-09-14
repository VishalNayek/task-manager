def main():
    tasks = []
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
            delete_tasks(tasks)
        elif(choice=='5'):
            print('Exited Task Manager.')
            break


def display_menu():
    print("====================")
    print("TASK MANAGER")
    print("====================")
    print("1. Create Task")
    print("2. View Tasks")
    print("3. Edit Task")
    print("4. Delete Task")
    print("5. Exit")


def create_tasks(tasks):
    if(tasks):
        getId = len(tasks) + 1
    else:
        getId = 1
    title = input("Enter the title of the task: ")
    description = input("Enter the description of the task: ")
    new_task = {
        "id": getId,
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
        taskFound = False
        inputId = int(input("Enter the Id of the task you want to edit: "))
        for task in tasks:
            if(task['id'] == inputId):
                task['title'] = input("Enter the new title: ")
                task['description'] = input("Enter the new description: ")
                taskFound = True
                print("Task has been updated.")
                break
        if(taskFound == False):
            print(f"No task found with id {inputId}")
    else:
        print("No tasks to edit.")


def delete_tasks(tasks):
    if(tasks):
            taskFound = False
            inputId = int(input("Enter the Id of the task you want to delete: "))
            for task in tasks:
                if(task['id'] == inputId):
                    tasks.remove(task)
                    taskFound = True
                    print("Task has been deleted.")
                    break
            if(taskFound == False):
                print(f"No task found with id {inputId}")
    else:
        print("No tasks to delete.")


main()