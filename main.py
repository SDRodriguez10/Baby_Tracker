#!/usr/bin/env python3
import os
import csv
from src import *
from feed_log import FeedLog

if __name__ == "__main__":
    file_names = ["feedLog.csv", "diaperLog.csv", "sleep_log.csv"]
    data_loc = "~/.baby_data"
    ex_path = os.path.expanduser(data_loc) # expanded path because ~
    
    # Data storage lists
    data_lists = []

    # If ~/.baby_data exists cool, if not make it
    if (os.path.exists(ex_path)):
        print("~/.baby_data found\n")
    else:
        print("~/.baby_data not found, creating it now")
        os.system("mkdir ~/.baby_data")
        gen_files(ex_path, file_names)
    
    feed_tracker = FeedLog()
    sleep_tracker = SleepLog()
    poop_tracker = DiaperLog()




if __debug__:
    print(data_lists)
