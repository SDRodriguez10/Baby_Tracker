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
    debug = 1
    file_names = ["feedLog.csv", "sleepLog.csv", "diaperLog.csv"]
    data_loc = "~/.baby_data"
    ex_path = os.path.expanduser(data_loc) # expanded path because ~

    # If ~/.baby_data exists cool, if not make it
    if (os.path.exists(ex_path)):
        print("~/.baby_data found\n")
    else:
        print("~/.baby_data not found, creating it now")
        os.system("mkdir ~/.baby_data")
        #gen_files(ex_path, file_names)
    
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
    print("Final feed state: ")
    print("Start time: ", feed_tracker.start_time)
    print("End time: ", feed_tracker.end_time)
    print("Counter: ", feed_tracker.counter)
    print("Toggle: ", feed_tracker.toggle)
    print("Selected number: ", feed_tracker.selected_number)

    print("Final sleep state: ")
    print("Start time: ", sleep_tracker.start_time)
    print("End time: ", sleep_tracker.end_time)
    print("Counter: ", sleep_tracker.counter)
    print("Toggle: ", sleep_tracker.toggle)
    print("Selected number: ", sleep_tracker.selected_number)

    print("Final poop state: ")
    print("Start time: ", poop_tracker.start_time)
    print("Diaper type: ", poop_tracker.diaper_type)
    print("Pee amount: ", poop_tracker.pee_amount)
    print("Poo amount: ", poop_tracker.poo_amount)
    print("Blowout: ", poop_tracker.blowout)
    print("Color: ", poop_tracker.color)
    
if __name__ == "__main__":
    main()
