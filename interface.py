class Interface:
    main_menu = ["1. view contact list", "2. search in contacts", "3. add a contact", "4. quit"]
    
    def __init__(self, core):
        self.core = core

    def show_menu(self):
        for x in range(len(self.main_menu)):
            print(self.main_menu[x])
        response = int(input("? "))
        return response