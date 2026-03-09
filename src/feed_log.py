from file_class import FileClass
from PyQt6.QtCore import QTime
import csv
class FeedLog(FileClass):
    def __init__(self, name, loc, debug):
        super().__init__(name, loc, debug)
        self.header = {0:'feed_start', 1:'feed_stop', 2:'feed_switch',
                       3:'feed_start_loc', 4:'feed_strength'}
        self.data_row = [None]*len(self.header)
        self.start_time = None
        self.end_time = None
        self.counter = 0
        self.toggle = 0
        self.selected_val = 1

    def clear_data(self):
        self.data_row = [None]*len(self.header)
        self.start_time = None
        self.end_time = None
        self.counter = 0
        self.toggle = 0
        self.selected_val = 1

    def add_data(self):
        """
        Feed log contains 4 pieces of data rn
            feed_start - start time
            feed_stop  - end time
            feed_switch? - how many times switch position
            feed_start_location - left(0), right(1)
            feed_strength - heuristic, how good latch? how much fed?idk
        """
        print("adding_data")
        return 0
    
    def record_time(self):
        time_now = QTime.currentTime().toString("HH:mm:ss")

        if self.start_time is None:
            self.start_time = time_now
            print(self.start_time)
        else:
            self.end_time = time_now
            print(self.end_time)

    def increment_counter(self):
        self.counter += 1
        print(self.counter)
    
    def toggle_value(self):
        self.toggle = 1 - self.toggle
        print(self.toggle)

    def set_number(self, n):
        self.selected_number = n
        print(self.selected_number)

    def publish_data(self):
        if self.end_time is None:
            return 0
        time_list = [self.start_time, self.end_time]
        pub_time_list = ["",""]
        for idx, time in enumerate(time_list):
            time_split = time.split(":")
            pub_time_list[idx] = time_split[0] + time_split[1]
        
        self.data_row[0] = pub_time_list[0]
        self.data_row[1] = pub_time_list[1]
        if None not in self.data_row:
            # publish
            print("working")
            clear_data()
            # reset
        else:
            # error
            print("error")



