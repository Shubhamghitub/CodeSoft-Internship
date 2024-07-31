class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone_number}, Email: {self.email}, Address: {self.address}"

class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self):
        name = input("Enter name: ")
        phone_number = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        self.contacts[name] = Contact(name, phone_number, email, address)
        print("Contact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for index, (name, contact) in enumerate(self.contacts.items(), start=1):
                print(f"{index}) {contact.name} - {contact.phone_number}")

    def search_contact(self):
        search_term = input("Enter name or phone number to search: ")
        found = False
        for contact in self.contacts.values():
            if search_term in contact.name or search_term in contact.phone_number:
                print(contact)
                found = True
        if not found:
            print("No matching contact found.")

    def update_contact(self):
        name = input("Enter the name of the contact to update: ")
        if name in self.contacts:
            print("Leave field empty to keep current value.")
            phone_number = input(f"New phone number (current: {self.contacts[name].phone_number}): ")
            email = input(f"New email (current: {self.contacts[name].email}): ")
            address = input(f"New address (current: {self.contacts[name].address}): ")
            contact = self.contacts[name]
            contact.phone_number = phone_number if phone_number else contact.phone_number
            contact.email = email if email else contact.email
            contact.address = address if address else contact.address
            print("Contact updated successfully!")
        else:
            print("Contact not found.")

    def delete_contact(self):
        name = input("Enter the name of the contact to delete: ")
        if name in self.contacts:
            del self.contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found.")

    def display_menu(self):
        menu = (
            "1. Add Contact\n"
            "2. View Contact List\n"
            "3. Search Contact\n"
            "4. Update Contact\n"
            "5. Delete Contact\n"
            "6. Exit"
        )
        print(menu)

def main():
    contact_book = ContactBook()
    
    while True:
        contact_book.display_menu()
        choice = input("Choose an option (1-6): ")
        
        if choice == '1':
            contact_book.add_contact()
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            contact_book.search_contact()
        elif choice == '4':
            contact_book.update_contact()
        elif choice == '5':
            contact_book.delete_contact()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please choose a number between 1 and 6.")

if __name__ == "__main__":
    main()
