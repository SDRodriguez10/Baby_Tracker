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
	with open(path, mode='r', newline='', encoding='utf-8') as file:
	    csv_reader = csv.reader(file, delimiter=',')
	    for row in csv_reader:
		print(row)




