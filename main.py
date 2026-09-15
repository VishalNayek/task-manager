from task_manager import TaskManager

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