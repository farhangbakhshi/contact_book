import json

from contact import Contact

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