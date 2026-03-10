#codebase
from file_class import FileClass
from PyQt6.QtCore import QTime
import csv
class FeedLog(FileClass):
    def __init__(self, name, loc, debug):
        """
        Feed log contains 5 pieces of data rn
            feed_start - start time
            feed_stop  - end time
            feed_switch? - how many times switch position
            feed_start_location - left(0), right(1)
            feed_strength - heuristic, how good latch? how much fed?idk
        """
        super().__init__(name, loc, debug)
        self.header = ['feed_start', 'feed_stop', 'feed_switch',
                       'feed_start_loc', 'feed_strength']
        self.data_row = [None]*len(self.header)
        self.start_time = None
        self.end_time = None
        self.counter = 0
        self.toggle = 0
        self.selected_number = 1
        if debug:
            print("DATA LIST")
            print(self.data_list)
        
    def clear_data(self):
        self.data_row = [None]*len(self.header)
        self.start_time = None
        self.end_time = None
        self.counter = 0
        self.toggle = 0
        self.selected_number = 1      

    def increment_counter(self):
        # TO count number of times switch position during feed, or number of feeds idk
        self.counter += 1
        if self.debug:
            print(self.counter)

    def toggle_value(self):
        # To toggle between left and right breast, 0 and 1
        self.toggle = 1 - self.toggle
        if self.debug:
            print("Toggle value: ")
            print(self.toggle)

    def write_data(self, data):
        with open(self.data_path, mode='a', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(data)

    def publish_data(self):
        if self.end_time is None:
            return 0
        
        if len(self.data_list) == 0:
            self.write_data(self.header)
        
        self.data_row[self.header.index('feed_start')] = self.start_time
        self.data_row[self.header.index('feed_stop')] = self.end_time
        self.data_row[self.header.index('feed_switch')] = self.counter
        self.data_row[self.header.index('feed_start_loc')] = self.toggle
        self.data_row[self.header.index('feed_strength')] = self.selected_number
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


