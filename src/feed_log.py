
from file_class import FileClass
class FeedLog(FileClass):
    def __init__(self, name, loc, debug):
        super().__init__(name, loc, debug)

    def add_data(self):

