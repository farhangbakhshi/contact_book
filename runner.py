from interface import Interface
from contact_book_core import Core
from file_handler import FileHandler

file_handler = FileHandler()
core = Core(file_handler)
interface = Interface(core)

interface.start()