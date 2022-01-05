class FileHandler:
    file_address = "data.json"

    def read_file(self):
        file = open(self.file_address, "rt")
        file_content = file.read()
        file.close()
        return file_content

    def write_file(self, file_content):
        file = open(self.file_address, "wt")
        file.write(file_content)
        file.close()