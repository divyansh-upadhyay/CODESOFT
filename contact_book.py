contacts = {}

def add_contact():
    name = input("Enter the contact's name: ")
    phone_number = input("Enter the phone number: ")
    email = input("Enter the email address: ")
    address = input("Enter the address: ")

    contacts[name] = {
        "phone_number": phone_number,
        "email": email,
        "address": address
    }
    print(f"{name} added to contacts.")


def view_contact_list():
    if not contacts:
        print("No contacts found.")
    else:
        print("Contact List:")
        for name, contact_info in contacts.items():
            print(f"Name: {name}, Phone: {contact_info['phone_number']}, Email: {contact_info['email']}, Address: {contact_info['address']}")


def search_contact():
    query = input("Enter the name , phone number , email or address to search: ")
    found = False
    for name, contact_info in contacts.items():
        if query in (name, contact_info['phone_number']):
            print(f"Name: {name}")
            print(f"Phone: {contact_info['phone_number']}")
            print(f"Email: {contact_info['email']}")
            print(f"Address: {contact_info['address']}")
            found = True
    if not found:
        print(f"No contact found for '{query}'.")


def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        phone_number = input("Enter the new phone number: ")
        email = input("Enter the new email address: ")
        address = input("Enter the new address: ")

        contacts[name]["phone_number"] = phone_number
        contacts[name]["email"] = email
        contacts[name]["address"] = address
        print(f"{name}'s contact details updated.")
    else:
        print(f"No contact found for '{name}'.")


def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"{name}'s contact deleted.")
    else:
        print(f"No contact found for '{name}'.")


while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contact_list()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Exiting the Contact Management System.")
        break
    else:
        print("Invalid choice. Please try again.")
