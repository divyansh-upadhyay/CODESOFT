# Initialize an empty list to store the to-do items
to_do_list = []

def display_to_do_list():
    if not to_do_list:
        print("Your to-do list is empty.")
    else:
        print("To-Do List:")
        for i, item in enumerate(to_do_list, 1):
            print(f"{i}. {item}")

def add_to_do_item():
    item = input("Enter the task you want to add: ")
    to_do_list.append(item)
    print(f"'{item}' has been added to your to-do list.")

def remove_to_do_item():
    display_to_do_list()
    if to_do_list:
        try:
            item_index = int(input("Enter the number of the task you want to remove: ")) - 1
            if 0 <= item_index < len(to_do_list):
                removed_item = to_do_list.pop(item_index)
                print(f"'{removed_item}' has been removed from your to-do list.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid task number.")
    else:
        print("Your to-do list is empty.")

def main():
    while True:
        print("\nOptions:")
        print("1. Display To-Do List")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_to_do_list()
        elif choice == "2":
            add_to_do_item()
        elif choice == "3":
            remove_to_do_item()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
