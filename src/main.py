#!/usr/bin/env python3
#codebase
import os
import csv
from diaper_gui import DiaperGui
from feed_log import FeedLog
from sleep_gui import SleepGui
from sleep_log import SleepLog
from diaper_log import DiaperLog
from feed_gui import FeedGui
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout
import sys

def main():
    debug = 0
    file_names = ["feedLog.csv", "sleepLog.csv", "diaperLog.csv"]
    data_loc = "~/.baby_data"
    ex_path = os.path.expanduser(data_loc) # expanded path because ~

    # If ~/.baby_data exists cool, if not make it
    if (os.path.exists(ex_path)):
        print("~/.baby_data found\n")
    else:
        print("~/.baby_data not found, creating it now")
        os.system("mkdir ~/.baby_data")
    
    # Create the tracker objects
    feed_tracker = FeedLog(file_names[0], data_loc, debug)
    sleep_tracker = SleepLog(file_names[1], data_loc, debug)
    poop_tracker = DiaperLog(file_names[2], data_loc, debug)

    # Create application instance
    app = QApplication(sys.argv)

    # Create instances of all GUIs
    sleep_gui = SleepGui(sleep_tracker)
    feed_gui = FeedGui(feed_tracker)
    diaper_gui = DiaperGui(poop_tracker)
    
    # Position windows side by side
    sleep_gui.setGeometry(100, 100, 300, 200)
    feed_gui.setGeometry(420, 100, 300, 400)
    diaper_gui.setGeometry(740, 100, 300, 500)
    
    # Show all the widgets
    sleep_gui.show()
    feed_gui.show()
    diaper_gui.show()

    # Start application's event loop
    sys.exit(app.exec())
    
if __name__ == "__main__":
    main()
