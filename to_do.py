tasks = []
def create_task():
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    task = {"title": title, "description": description, "completed": False}
    tasks.append(task)
    print(f"Task '{title}' added.")

def update_task():
    title = input("Enter the title of the task to update: ")
    for task in tasks:
        if task["title"] == title:
            new_description = input("Enter the new task description: ")
            task["description"] = new_description
            print(f"Task '{title}' updated.")
            return
    print(f"Task '{title}' not found.")
def track_task():
    print("To-Do List:")
    for task in tasks:
        status = "Completed" if task["completed"] else "Not Completed"
        print(f"Title: {task['title']}")
        print(f"Description: {task['description']}")
        print(f"Status: {status}")
        print()
while True:
    print("\nOptions:")
    print("1. create Task")
    print("2. Update Task")
    print("3. track Tasks")
    print("4. Quit")

    choice = input("Select an option (1/2/3/4): ")

    if choice == "1":
        create_task()
    elif choice == "2":
        update_task()
    elif choice == "3":
        track_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")