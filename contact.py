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
        self.id = str(uuid.uuid4())
