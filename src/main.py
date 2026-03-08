#!/usr/bin/env python3
import os
import csv
from feed_log import FeedLog
from sleep_log import SleepLog
from diaper_log import DiaperLog
from gui import BabyGui
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
import sys

def main():
    debug = 1
    file_names = ["feedLog.csv", "diaperLog.csv", "sleepLog.csv"]
    data_loc = "~/.baby_data"
    ex_path = os.path.expanduser(data_loc) # expanded path because ~

    # If ~/.baby_data exists cool, if not make it
    if (os.path.exists(ex_path)):
        print("~/.baby_data found\n")
    else:
        print("~/.baby_data not found, creating it now")
        os.system("mkdir ~/.baby_data")
        gen_files(ex_path, file_names)
    
    # Create the tracker objects
    feed_tracker = FeedLog(file_names[0], data_loc, debug)
    sleep_tracker = SleepLog(file_names[1], data_loc, debug)
    poop_tracker = DiaperLog(file_names[2], data_loc, debug)

    # Create application instance
    app = QApplication(sys.argv)

    # Create instance of Window
    baby_gui = BabyGui()
    
    # Show all the widgets
    baby_gui.show()

    # Start application's event loop
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
