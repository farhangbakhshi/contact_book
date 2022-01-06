import json

from contact import Contact

def key_function(contact):
        return contact.get_name()

class Core:

    file_handler = None
    contact_list = None

    def __init__(self, file_handler):
        self.file_handler = file_handler
        self.contact_list = json.loads(file_handler.read_file())
        
        for x in range(len(self.contact_list)):
            self.contact_list[x] = Contact(self.contact_list[x]["name"], self.contact_list[x]["number"], self.contact_list[x]["address"])


    
    def add_contact(self, name, number, address):
        new_contact = Contact(name, number, address)
        self.contact_list.append(new_contact)
        self.contact_list.sort(key = key_function)
        list_for_json = []
        for x in range(len(self.contact_list)):
            contact_in_dict = {"name":self.contact_list[x].get_name(), "number":self.contact_list[x].get_number(), "address":self.contact_list[x].get_address()}
            list_for_json.append(contact_in_dict)
        self.file_handler.write_file(json.dumps(list_for_json))

    def get_contact_names(self):
        names_list = []
        for x in self.contact_list:
            names_list.append(x.get_name())
        return names_list

    def search(self, s_phrase, in_core_search = False):
        results_list = []
        for x in self.contact_list:
            if s_phrase in x.get_name():
                if in_core_search:
                    results_list.append(x)
                else:
                    results_list.append(x.get_name())
        return results_list

    def get_contact_details(self, index, s_phrase):
        if s_phrase == "":
            details = [self.contact_list[index - 1].get_name(), self.contact_list[index - 1].get_number(), self.contact_list[index - 1].get_address()]
            return details
        else:
            results = self.search(s_phrase, True)
            details = [results[index - 1].get_name(), results[index - 1].get_number(), results[index - 1].get_address()]
            return details