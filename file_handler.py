class FileHandler:
    def __init__(self):
        self.file = open("contacts.json", "rt")
        # print(self.file.read())