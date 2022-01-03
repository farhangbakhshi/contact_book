from contact import Contact

class Interface:
    main_menu = ["1. view contact list", "2. search in contacts", "3. add a contact", "4. quit"]
    contact_view_menu = ["1. edit", "2. delete"]

    def __init__(self, core):
        self.core = core

    def show_menu(self):
        for x in range(len(self.main_menu)):
            print(self.main_menu[x])
        response = int(input("? "))
        return response

    def start(self):
        while True:
            user_choice = self.show_menu()
            if user_choice == 4:
                quit()
            elif user_choice == 3:
                self.add_contact()
            elif user_choice == 1:
                contact_list = self.core.get_contact_names()
                for x in contact_list:
                    print(x)

    def add_contact(self):
        new_contact_name = input("what is the name? ")
        new_contact_number = input("what is the number? ")
        new_contact_address = input("what is the address? ")
        self.core.add_contact(new_contact_name, new_contact_number, new_contact_address)