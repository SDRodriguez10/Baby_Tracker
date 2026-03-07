# This is the class that manages the feeding schedule add/update/remove

import numpy as np
from pathlib import Path
import csv

class FeedLog:
    def __init__(self):
        # init filename and location
        self.file_name = "feed_log.csv"
        self.file_loc  = "~/.baby_data"
        # Check if file exists

        self.data_path = gen_path()

    def gen_path(self):
        # If this is the first time running then gen the file
        glued_path = self.file_loc + "/" + self.file_loc
        return 0

    def get_data(self):
        return 0
