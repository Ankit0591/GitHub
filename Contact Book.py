class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}"

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        contact = Contact(name, phone, email, address)
        self.contacts.append(contact)
        print("Contact added!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts in the contact book.")
            return
        for contact in self.contacts:
            print(contact)

    def search_contact(self, search_term):
        found_contacts = [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone]
        if found_contacts:
            for contact in found_contacts:
                print(contact)
        else:
            print("No contacts found.")

    def update_contact(self, search_term):
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone:
                print("Contact found. Enter new details.")
                contact.name = input("Name: ")
                contact.phone = input("Phone: ")
                contact.email = input("Email: ")
                contact.address = input("Address: ")
                print("Contact updated!")
                return
        print("No contact found with the given details.")

    def delete_contact(self, search_term):
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone:
                self.contacts.remove(contact)
                print("Contact deleted!")
                return
        print("No contact found with the given details.")

def main():
    contact_book = ContactBook()
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone, email, address)
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            contact_book.search_contact(search_term)
        elif choice == '4':
            search_term = input("Enter name or phone number to update: ")
            contact_book.update_contact(search_term)
        elif choice == '5':
            search_term = input("Enter name or phone number to delete: ")
            contact_book.delete_contact(search_term)
        elif choice == '6':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
