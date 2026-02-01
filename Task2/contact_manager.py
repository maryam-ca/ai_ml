# contact_manager.py
# File-based Contact Manager

FILE = "contacts.txt"


def add_contact(name, phone):
    try:
        # Append mode
        with open(FILE, "a") as f:
            f.write(f"{name},{phone}\n")
        print("Contact added")
    except Exception as e:
        print("Error:", e)


def view_contacts():
    try:
        # Read mode
        with open(FILE, "r") as f:
            for line in f:
                name, phone = line.strip().split(",")
                print(f"Name: {name}, Phone: {phone}")
    except FileNotFoundError:
        print("No contacts found")


def main():
    while True:
        print("\n1 Add Contact\n2 View Contacts\n3 Exit")
        choice = input("Choice: ")

        if choice == "1":
            add_contact(input("Name: "), input("Phone: "))
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
