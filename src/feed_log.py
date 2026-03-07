# This is the class that manages the feeding schedule add/update/remove

import numpy as np
from pathlib import Path
import csv

class FeedLog:
    def __init__(self):
    # init filename and location
    self.file_name = "feed_log.csv"
    self.file_loc  = "./data"
    file_path = Path(self.file_loc + "/" + self.file_name)
    
    if file_path.isfile():
        print("Hello World")
    else:
        os.system("mkdir data/")



