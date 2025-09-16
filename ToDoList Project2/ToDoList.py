tasks = [] # List to store tasks

def add_task(task):
    # Add the task at last in the list
    tasks.append(task)
    print(f'Task "{task}" added.')

def list_tasks():
    # List all tasks with their index
    if tasks:
        print("Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f" {i}. {task}")
    else:
        print("No tasks found.")
def remove_task(index):
    # Remove the task from the list if it exists using the index
    if 0 <= index < len(tasks):
        removed_task = tasks.pop(index)
        print(f'Task "{removed_task}" removed.')
    else:
        print(f'Invalid task index: {index}')

def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. List Tasks")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            # Add a new task
            task = input("Enter the task to add: ")
            add_task(task)
        elif choice == '2':
            # If task list is empty, notify user
            if not tasks:
                print("No tasks to remove.")
                continue
            # Show tasks and ask for index to remove
            list_tasks()
            task = input("Enter the task number to remove: ")
            remove_task(int(task) - 1)
        elif choice == '3':
            # List all tasks with their index
            list_tasks()
        elif choice == '4':
            # Exit the program
            print("Exiting To-Do List.")
            exit()
        else:
            print("Invalid choice. Please try again.")
# Run the main function if this script is executed            
if __name__ == "__main__":
    main()