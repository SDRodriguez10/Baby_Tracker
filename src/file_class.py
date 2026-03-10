#codebase
# This is the class that manages the feeding schedule add/update/remove

from pathlib import Path
import csv
import os
from PyQt6.QtCore import QTime
import csv
class FileClass:
    def __init__(self, name, loc, debug):
        # init filename and location
        self.file_name = name
        self.file_loc  = loc
        # Check if file exists
        self.data_path = ""
        self.data_list = []
        self.gen_path()
        self.set_data()
        self.debug = debug
        if (self.debug):
            self.get_data()

    def gen_path(self):
        # If this is the first time running then gen the file path
        glued_path = self.file_loc + "/" + self.file_name
        self.data_path = os.path.expanduser(glued_path)
        # If the file doesn't exist make it, if it does leave it alone
        open(self.data_path, "a").close
        return 0

    def set_data(self):
        if (os.path.exists(self.data_path)):
            print(str(self.file_name) + " found! Importing existing data")
            with open(self.data_path, mode='r', newline='', encoding='utf-8') as csv_file:
                dict_reader = csv.DictReader(csv_file)
                for row in dict_reader:
                    self.data_list.append(row)
        return 0

    def get_data(self):
        print("Printing " + self.file_name + ":")
        for row in self.data_list:
            print(row)
        print("\n")
        return 0
    
    def record_time(self):
        time_now = QTime.currentTime().toString("HH:mm:ss")

        if self.start_time is None:
            self.start_time = time_now
            time_split = self.start_time.split(":")
            self.start_time = time_split[0] + ":" + time_split[1]
            if self.debug:
                print(self.start_time)
        else:
            self.end_time = time_now
            time_split = self.end_time.split(":")
            self.end_time = time_split[0] + ":" + time_split[1]
            if self.debug:
                print("End time: ")
                print(self.end_time)

    def set_number(self, n):
        self.selected_number = n
        if self.debug:
            print("Selected number: ")
            print(self.selected_number)
    
    
    
    
