#codebase
from file_class import FileClass
from PyQt6.QtCore import QTime
import csv
class SleepLog(FileClass):
    def __init__(self, name, loc, debug):
        super().__init__(name, loc, debug)
        self.header = ['sleep_start', 'sleep_end', 'sleep_quality']
        self.data_row = [None]*len(self.header)
        self.start_time = None
        self.end_time = None
        self.selected_number = 1
        if debug:
            print("DATA LIST")
            print(self.data_list)
    
    def publish_data(self):
        if self.end_time is None:
            return 0
        
        if len(self.data_list) == 0:
            self.write_data(self.header)
        
        # Map data to correct header value
        self.data_row[self.header.index('sleep_start')] = self.start_time
        self.data_row[self.header.index('sleep_end')] = self.end_time
        self.data_row[self.header.index('sleep_quality')] = self.selected_number
        if None not in self.data_row:
            # publish
            print("Publishing data to " + self.file_name)
            print(self.data_row)
            self.write_data(self.data_row)
            self.clear_data()
            # reset
        else:
            # error
            print("error")
            print(self.data_row)

    def clear_data(self):
        self.data_row = [None]*len(self.header)
        self.start_time = None
        self.end_time = None
        self.selected_number = 1
        
    def write_data(self, data):
        with open(self.data_path, mode='a', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(data)