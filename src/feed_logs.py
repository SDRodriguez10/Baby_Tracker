
from file_class import FileClass
class FeedLogs(FileClass):
    def __init__(self, name, loc, debug):
        super().__init__(name, loc, debug)

    def print_data(self):
        print(self.data_list)
