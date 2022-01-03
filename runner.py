import json
from contact import Contact
from interface import Interface
from contact_book_core import Core
from file_handler import FileHandler

file_handler = FileHandler()
core = Core(file_handler)
interface = Interface(core)

while True:
    user_choice = interface.show_menu()
    if user_choice == 4:
        quit()
    elif user_choice == 3:
        new_contact_name = input("what is the name? ")
        new_contact_number = input("what is the number? ")
        new_contact_address = input("what is the address? ")
        new_contact = Contact(new_contact_name, new_contact_number, new_contact_address)
        print(new_contact)


