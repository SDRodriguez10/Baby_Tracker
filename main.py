#!/usr/bin/env python3
import os
import csv
from src import *
def get_data(dir_path, file_names):
    for fi_name in file_names:
        glued_path = dir_path + "/" + fi_name
        ex_path = os.path.expanduser(glued_path)
        if (os.path.exists(ex_path)):
            print(str(fi_name) + " found! Importing existing data")
            with open(ex_path, mode='r', newline='', encoding='utf-8') as csv_file:
                dict_reader = csv.DictReader(csv_file)
                for row in dict_reader:
                    feed_list.append(row)
                    
        else:
            print(".baby_data not found! Generating new data folder")
            os.system("mkdir ~/.baby_data")
            os.system("touch ~/.baby_data/data.csv")
    return 0

def gen_files(dir_path, file_names):
    for fi_name in file_names:
        
        # cat the file name and dir path together
        glued_path = dir_path + "/" + fi_name
        # Expand the ~/ part 
        ex_path = os.path.expanduser(glued_path)

        # Create empty file if it does not exist
        open(ex_path, "a").close()
    return 0


if __name__ == "__main__":
    file_names = ["feedLog.csv", "diaperLog.csv", "sleep_log.csv"]
    data_loc = "~/.baby_data"
    ex_path = os.path.expanduser(data_loc) # expanded path because ~
    
    # Data storage lists
    data_lists = []

    # If ~/.baby_data exists, get data from it, if not init it
    if (os.path.exists(ex_path)):
        print("~/.baby_data found, extracting data\n")
        data_lists = get_data(ex_path, file_names)
    else:
        print("~/.baby_data not found, creating it now")
        os.system("mkdir ~/.baby_data")
        gen_files(ex_path, file_names)
    
    feed_tracker = FeedLog()
    sleep_tracker = SleepLog()
    poop_tracker = DiaperLog()




if __debug__:
    print(data_lists)
