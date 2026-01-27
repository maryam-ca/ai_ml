# contact_manager.py
# File-based Contact Manager

FILE_NAME = "contacts.txt"


def add_contact(name, phone):
    try:
        with open(FILE_NAME, "a") as file:
            file.write(f"{name},{phone}\n")
        print("Contact added successfully.")
    except Exception as e:
        print("Error:", e)


def view_contacts():
    try:
        with open(FILE_NAME, "r") as file:
            contacts = file.readlines()
            if not contacts:
                print("No contacts found.")
            for contact in contacts:
                name, phone = contact.strip().split(",")
                print(f"Name: {name}, Phone: {phone}")
    except FileNotFoundError:
        print("No contact file found.")


def main():
    while True:
        print("\n1. Add Contact")
        print("2. View Contacts")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            add_contact(name, phone)
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            break
        else:
            print("Invalid choice")


main()
