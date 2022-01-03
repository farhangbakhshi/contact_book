import json

from contact import Contact

def key_function(contact):
        return contact.get_name()

class Core:
    def __init__(self, file_handler):
        self.file_handler = file_handler
        self.contactlist = json.loads(file_handler.read_file())
        
        for x in range(len(self.contactlist)):
            contact_name = self.contactlist[x]["name"]
            contact_number = self.contactlist[x]["number"]
            contact_address = self.contactlist[x]["address"]
            contact = Contact(contact_name, contact_number, contact_address)
            self.contactlist[x] = contact
        # print(type(self.contactlist[0]))

    
    def add_contact(self, name, number, address):
        new_contact = Contact(name, number, address)
        self.contactlist.append(new_contact)
        self.contactlist.sort(key = key_function)
        list_for_json = []
        for x in range(len(self.contactlist)):
            contact_in_dict = {"name":self.contactlist[x].get_name(), "number":self.contactlist[x].get_number(), "address":self.contactlist[x].get_address()}
            list_for_json.append(contact_in_dict)
        self.file_handler.write_file(json.dumps(list_for_json))

    def get_contact_names(self):
        names_list = []
        for x in self.contactlist:
            names_list.append(x.get_name())
        return names_list

    def search(self, s_phrase):
        results_list = []
        for x in self.contactlist:
            if s_phrase in x.get_name():
                results_list.append(x.get_name())
        return results_list