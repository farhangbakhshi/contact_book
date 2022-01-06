import uuid

class Contact:

    neme = None
    number = None
    address = None
    id = None

    def __init__(self, name, number, address):
        self.name = name
        self.number = number
        self.address = address
        self.id = uuid.uuid4()

    def get_name(self):
        return self.name

    def get_number(self):
        return self.number

    def get_address(self):
        return self.address

    def set_name(self, new_name):
        self.name = new_name

    def set_number(self, new_number):
        self.number = new_number

    def set_address(self, new_address):
        self.address = new_address