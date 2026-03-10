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
        
        time_list = [self.start_time, self.end_time]
        pub_time_list = ["",""]
        for idx, time in enumerate(time_list):
            time_split = time.split(":")
            pub_time_list[idx] = time_split[0] + time_split[1]
        
        self.data_row[self.header.index('sleep_start')] = pub_time_list[0]
        self.data_row[self.header.index('sleep_end')] = pub_time_list[1]
        self.data_row[self.header.index('sleep_quality')] = self.selected_number
        if None not in self.data_row:
            # publish
            print("Publishing data to " + self.file_name)
            print(self.data_row)
            self.write_data(self.data_row)
            self.clear_data()
            print("Data Cleared")
            print(self.data_row)
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