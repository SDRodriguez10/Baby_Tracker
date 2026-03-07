# This is the class that manages the feeding schedule add/update/remove

from pathlib import Path
import csv

class FeedLog:
    def __init__(self):
        # init filename and location
        self.file_name = "feed_log.csv"
        self.file_loc  = "~/.baby_data"
        # Check if file exists
        self.data_path = ""
        self.feed_list = []
        gen_path()
        set_data()
        get_data()

    def gen_path(self):
        # If this is the first time running then gen the file path
        glued_path = self.file_loc + "/" + self.file_name
        self.data_path = os.path.expanduser(glued_path)
        # If the file doesn't exist make it, if it does leave it alone
        open(self.data_path, "a").close
        return 0

    def set_data(self):
        if (os.path.exists(self.data_path)):
            print(std(self.file_name) + " found! Importing existing data")
            with open(self.data_path, mode='r', newline='', encoding='utf-8') as csv_file:
                dict_reader = csv.DictReader(csv_file)
                for row in dict_reader:
                    self.feed_list.append(row)
        return 0

    def get_data(self):
        for row in self.feed_list:
            print(row)
        return 0
