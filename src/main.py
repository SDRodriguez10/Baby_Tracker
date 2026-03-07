#!/usr/bin/env python3
import os

if __name__ == "__main__":
    data_loc = "~/.baby_data/data"
    ex_path = os.path.expanduser(data_loc) # expanded path because ~
    if os.path.exists(ex_path):
        print("Hello World")
    else:
        os.system("mkdir ~/.baby_data")
        os.system("mkdir ~/.baby_data/data")

