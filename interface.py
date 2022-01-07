from contact_book_core import Core


class Interface:
    menus = {
        "main_menu": [
            "1. view contact list",
            "2. search in contacts",
            "3. add a contact",
            "4. quit",
        ],
        "contact_list_view_menu": [
            "choose a contact by number to show details or use 0 to go back to main menu."
        ],
        "contact_details_view_menu": ["1. edit", "2. delete", "0. main menu"],
        "edit_menu": ["1. name", "2. number", "3. address"],
    }

    def __init__(self, core: Core):
        self.core = core

    def show_menu(self, menu_name):
        """
        this method is made only to clean up the clutter in start()
        """
        # algorithm is pretty obvious.

        for x in self.menus[menu_name]:
            print(x)

        user_choice = int(input("? "))
        return user_choice

    def start(self):
        """
        this is the method that uses core to run all user requests.
        """
        # this while True loop is used to constantly get user requests while staying in the program until the user chooses to quit the program
        while True:
            user_choice = self.show_menu("main_menu")

            if user_choice == 1:
                # in this case we first have to get the list of all contacts' IDs
                id_list = self.core.get_contacts_id_list()
                self.contact_list_choices(id_list)

            elif user_choice == 2:
                # first we need a search phrase
                s_phrase = input("enter the phrase you want to search for. \n")
                results_id_list = self.core.search(s_phrase)
                self.contact_list_choices(results_id_list)

            elif user_choice == 3:
                self.add_contact()

            elif user_choice == 4:
                quit()

    def add_contact(self):
        """
        this method, like many others, is made to avoid the clutter in start() method
        """
        # algorithm is pretty obvious.
        new_contact_name = input("what is the name? ")
        new_contact_number = input("what is the number? ")
        new_contact_address = input("what is the address? ")
        self.core.add_contact(
            new_contact_name, new_contact_number, new_contact_address
        )

    def contact_list_choices(self, id_list):
        """
        this method, like many others, is made to avoid the clutter in start() method
        """
        # first we have to make a list of lists in which each item is a list of the contact's other details. remember that these two lists have similar indexes for each contact. one storing the ID and the other a list of that ID's other attributes.
        details_list = []
        for x in id_list:
            details_list.append(self.core.get_contact_details(x))
        # then we print the list of names and ask the user to either choose one or go back to the main menu
        for x in range(len(details_list)):
            print(str(x + 1) + ". " + details_list[x][0])
        user_contact_choice = self.show_menu("contact_list_view_menu")
        # now we have to deal with that user choice
        if user_contact_choice == 0:
            return
        else:
            print("name: " + details_list[user_contact_choice - 1][0])
            print("number: " + details_list[user_contact_choice - 1][1])
            print("address: " + details_list[user_contact_choice - 1][2])
        # now we show the user another menu to choose what to do with this contact
        user_choice_in_detail_view = self.show_menu("contact_details_view_menu")
        # and again, dealing with that choice...
        if user_choice_in_detail_view == 0:
            return
        elif user_choice_in_detail_view == 1:
            # this one will need some info that should be gotten from the user before we call an edit for that contact, so this one goes to a method inside this same class first
            self.edit_contact(id_list[user_contact_choice - 1])
            print("user successfully edited.")
        elif user_choice_in_detail_view == 2:
            # but this one can directly go to core. we don't need any more info.
            self.core.delete_contact(id_list[user_contact_choice - 1])
            print("user deleted.")
        # ... and, it seems like we are finally done with the option.

    def edit_contact(self, id):
        """
        this method is made to view the menu and ask the question about the edit in contact, and then return to the contact_list_choices method (where it's called)
        """
        # first we use our dear show_menu to show the menu
        detail_to_edit = self.show_menu("edit_menu")
        # then we ask the right question
        if detail_to_edit == 1:
            new_detail = input("what is the new name?\n")
        elif detail_to_edit == 2:
            new_detail = input("what is the new number?\n")
        elif detail_to_edit == 3:
            new_detail = input("what is the new address?\n")
        # then we give it to the core (where this detail_to_edit number means the same thing as above)
        self.core.edit_contact(id, detail_to_edit, new_detail)
