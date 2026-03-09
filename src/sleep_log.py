#codebase
from file_class import FileClass
class SleepLog(FileClass):
    def __init__(self, name, loc, debug):
        super().__init__(name, loc, debug)
        self.header = ['sleep_start', 'sleep_end', 'sleep_duration',
                       'sleep_quality']