
class SleepLog:
    def __init__(self):
        # init filename and location
        self.file_name = "sleepLog.csv"
        self.file_loc  = "~/.baby_data"
        
        self.data_path = ""
        self.sleep_list = []
        self.gen_path()
        self.set_data()
        if (debug):
            self.get_data()
