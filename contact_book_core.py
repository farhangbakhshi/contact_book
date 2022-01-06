import json

from contact import Contact


def key_function(contact):
    '''
    this function gets a contact and returns its name to be used in a sort function as the key to sort. SORT IS DONE IN ADD_CONTACT().
    '''
    return contact.name

class Core:

    file_handler = None
    contact_list = None

    def __init__(self, file_handler):
        #setting the attributes. for now, we read the file and use contact_list for the dictionaries read from the json file.
        self.file_handler = file_handler
        self.contact_list = json.loads(file_handler.read_file())
        #now we replace each dictionary in contact_list with a Contact object made with the info from the same dictionary.
        for x in range(len(self.contact_list)):
            self.contact_list[x] = Contact(self.contact_list[x]["name"], self.contact_list[x]["number"], self.contact_list[x]["address"])


    
    def add_contact(self, name, number, address):
        '''
        called from interface. given the variables needed for initializing the contact, it creates the contact and adds it to the contact_list and data file.
        '''
        #making the new contact
        new_contact = Contact(name, number, address)
        #appending it to the contact_list and sorting that list to make it ready for writing to the file and possible future view_contact_list actions
        self.contact_list.append(new_contact)
        self.contact_list.sort(key = key_function)
        #preparing the string for file by turning each contact into a dictionary and adding them all to a list
        list_for_json = []
        for x in range(len(self.contact_list)):
            contact_in_dict = {"name":self.contact_list[x].name, "number":self.contact_list[x].number, "address":self.contact_list[x].address, "id":self.contact_list[x].id}
            list_for_json.append(contact_in_dict)
        #now we use dumps() to prepare the list for the json file and then call write_file() to save the new list to the file.
        self.file_handler.write_file(json.dumps(list_for_json))

    def get_contacts_id_list(self):
        '''
        this method is for when interface needs to view all contacts' list. we give it the IDs and it will get names and details later.
        '''
        id_list = []
        for x in self.contact_list:
            id_list.append(x.id)
        return id_list

    def search(self, s_phrase):
        '''
        for when interface needs a list of contacts whose names contain a special set of characters. called from interface, returns IDs.
        '''
        #algorithm is pretty obvious.
        results_list = []
        for x in self.contact_list:
            if s_phrase in x.name:
                results_list.append(x.id)
        return results_list

    def get_contact_details(self, id):
        '''
        this method is used by interface to get the details of each contact using the id. at this stage, we get all of the details on all of the contacts and later only view the details of the selected one from that list.
        there is also the option of using a get_contact_name(self, id) method only for names, and only getting the other details later when one contact is selected
        '''
        #first we have to find that contact in our contact_list
        intended_contact:Contact = None
        for x in self.contact_list:
            if x.id == id:
                intended_contact = x
                break
        #then we return the other details of that contact's profile to the interface
        details = [intended_contact.name, intended_contact.number, intended_contact.address]
        return details
