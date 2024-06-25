class Contact:
    def __init__(self, id, name, phone, email):
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email

    def update_contact(self, phone = None, email = None):
        if phone:
            self.phone = phone
        if email:
            self.email = email

    def __str__(self):
        return f"{self.id}, {self.name}, {self.phone}, {self.email}"
        

class phoneBook:
    def __init__(self):
        self.contacts = []
        self.load_contacts()
    
    def contact_menu(self):
        while True:
            print("1. Add a contact")
            print("2. Update a contact")
            print("3. Delete a contact")
            print("4. View all contacts")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_contact()
            if choice == '2':
                self.update_contact()
            if choice == '3':
                self.delete_contact()
            if choice == '4':
                self.view_contacts()
            elif choice == '5':
                self.save_contacts()
                print("Exiting program....")
                break
            else:
                print("Invalid choice. Enter a number")

    def add_contact(self):
        contact_name = input("Please enter a full name with a space in between: ")
        phone_number = input("Please enter the phone number: ")
        email = input("Please enter the email address: ")

        if self.contacts:
            new_id = self.contacts[-1].id + 1
        else:
            new_id = 1

        new_contact = Contact(new_id, contact_name, phone_number, email)
        self.contacts.append(new_contact)
        print(f"Contact {contact_name} added successfully.")

        

    def update_contact(self):
        self.view_contacts()
        contact_id = int(input("Select the ID of the contact you would like to update: "))
       
        found = False
        for contact in self.contacts:
            if contact.id == contact_id:
                found = True
                new_phone = input(f"Enter new phone number for {contact.name}: ")
                new_email = input(f"Enter new email for {contact.name}: ")
                contact.update_contact(phone=new_phone, email=new_email)
                print(f"Contact {contact.name} updated successfully.")
                break
        
        if not found:
            print("Contact not found.")


    def view_contacts(self):
        if not self.contacts:
            print("No contacts available")
        else:
            for contact in self.contacts:
                print(contact)

    def save_contacts(self):
        with open('contacts.txt', 'w') as file:
            for contact in self.contacts:
                file.write(str(contact) + "\n") 
    
    def load_contacts(self):
        try:
            with open('contacts.txt', 'r') as file:
                for line in file:
                    id, name, phone, email = line.strip().split(',')
                    self.contacts.append(Contact(int(id), name, phone, email))
        except FileNotFoundError:
            print("No contacts file found. Starting with an empty phone book.")


    def delete_contact(self):
        self.view_contacts()
        contact_id = int(input("Select the ID of the contact you would like to delete: "))

        found = False
        for contact in self.contacts:
            if contact.id == contact_id:
                found = True
                self.contacts.remove(contact)
                print(f"Contact {contact.name} deleted successfully.")
                break
        if not found:
            print("Contact not found")
        

if __name__ == "__main__":
    phone_book = phoneBook()
    phone_book.contact_menu()