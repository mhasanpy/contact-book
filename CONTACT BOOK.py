# contact_book.py
import json
import re

class ContactBook:
    def __init__(self):
        self.contacts = {}
        self.filename = "contacts.json"
        self.load_contacts()
    
    def validate_phone(self, phone):
        """Validate phone number"""
        return re.match(r'^\+?1?\d{9,15}$', phone)
    
    def validate_email(self, email):
        """Validate email address"""
        return re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)
    
    def add_contact(self):
        """Add a new contact"""
        print("\n📇 Add New Contact")
        
        name = input("Name: ").strip()
        if not name:
            print("❌ Name is required!")
            return
        
        if name in self.contacts:
            print("❌ Contact already exists!")
            return
        
        phone = input("Phone: ").strip()
        if not self.validate_phone(phone):
            print("⚠️ Invalid phone number format!")
        
        email = input("Email: ").strip()
        if email and not self.validate_email(email):
            print("⚠️ Invalid email format!")
        
        address = input("Address: ").strip()
        
        self.contacts[name] = {
            "phone": phone,
            "email": email,
            "address": address
        }
        
        self.save_contacts()
        print(f"✅ Contact '{name}' added successfully!")
    
    def search_contacts(self):
        """Search contacts by name"""
        search = input("\n🔍 Enter name to search: ").strip().lower()
        
        found = [(name, details) for name, details in self.contacts.items() 
                if search in name.lower()]
        
        if not found:
            print("No contacts found!")
            return
        
        print(f"\n📋 Found {len(found)} contact(s):")
        print("="*50)
        for name, details in found:
            print(f"\n👤 Name: {name}")
            print(f"📞 Phone: {details['phone']}")
            print(f"📧 Email: {details['email']}")
            print(f"🏠 Address: {details['address']}")
            print("-"*30)
    
    def view_all_contacts(self):
        """View all contacts"""
        if not self.contacts:
            print("No contacts found!")
            return
        
        print("\n📋 ALL CONTACTS")
        print("="*50)
        for i, (name, details) in enumerate(sorted(self.contacts.items()), 1):
            print(f"{i:2}. {name:<20} 📞 {details['phone']}")
    
    def update_contact(self):
        """Update existing contact"""
        name = input("\nEnter contact name to update: ").strip()
        
        if name not in self.contacts:
            print("❌ Contact not found!")
            return
        
        print(f"\nUpdating contact: {name}")
        print("Press Enter to keep current value")
        
        phone = input(f"Phone ({self.contacts[name]['phone']}): ").strip()
        if phone:
            self.contacts[name]['phone'] = phone
        
        email = input(f"Email ({self.contacts[name]['email']}): ").strip()
        if email:
            self.contacts[name]['email'] = email
        
        address = input(f"Address ({self.contacts[name]['address']}): ").strip()
        if address:
            self.contacts[name]['address'] = address
        
        self.save_contacts()
        print("✅ Contact updated!")
    
    def delete_contact(self):
        """Delete a contact"""
        name = input("\nEnter contact name to delete: ").strip()
        
        if name not in self.contacts:
            print("❌ Contact not found!")
            return
        
        confirm = input(f"Delete '{name}'? (y/n): ").lower()
        if confirm == 'y':
            del self.contacts[name]
            self.save_contacts()
            print("✅ Contact deleted!")
    
    def save_contacts(self):
        """Save contacts to file"""
        with open(self.filename, 'w') as f:
            json.dump(self.contacts, f, indent=2)
    
    def load_contacts(self):
        """Load contacts from file"""
        try:
            with open(self.filename, 'r') as f:
                self.contacts = json.load(f)
        except FileNotFoundError:
            self.contacts = {}

def main():
    book = ContactBook()
    while True:
        print("\n📇 CONTACT BOOK MENU")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Choose (1-6): ")
        
        if choice == "1":
            book.add_contact()
        elif choice == "2":
            book.view_all_contacts()
        elif choice == "3":
            book.search_contacts()
        elif choice == "4":
            book.update_contact()
        elif choice == "5":
            book.delete_contact()
        elif choice == "6":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()