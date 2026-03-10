#codebase
import csv

from file_class import FileClass
class DiaperLog(FileClass):
    def __init__(self, name, loc, debug):
        """
        Diaper log contains 6 pieces of data rn
            diaper_time - time of diaper change
            diaper_type - pee(0), poo(1), both(2)
            pee_amount - how much pee? 1-5 (only triggered if diaper_type is pee or both)
            poo_amount - how much poo? 1-5 (only triggered if diaper_type is poo or both)
            blowout - boolean, did blowout occur?
            color - color of pee or poo, 5 colors?
        """
        super().__init__(name, loc, debug)
        self.header = ['diaper_time', 'diaper_type', 'pee_amount',
                       'poo_amount', 'blowout', 'color']
        self.data_row = [None]*len(self.header)
        self.start_time = None
        self.diaper_type = None
        self.pee_amount = None
        self.poo_amount = None
        self.blowout = None
        self.color = None
        if debug:
            print("DATA LIST")
            print(self.data_list)
    
    def set_diaper_type(self, t):
        self.diaper_type = t
        if self.debug:
            print("Selected diaper type: ")
            print(self.diaper_type)
    
    def set_pee_amount(self, a):
        self.pee_amount = a
        if self.debug:
            print("Selected pee amount: ")
            print(self.pee_amount)

    def set_poo_amount(self, a):
        self.poo_amount = a
        if self.debug:
            print("Selected poo amount: ")
            print(self.poo_amount)
    
    def set_blowout(self, b):
        self.blowout = b
        if self.debug:
            print("Selected blowout: ")
            print(self.blowout)
    
    def set_color(self, c):
        self.color = c
        if self.debug:
            print("Selected color: ")
            print(self.color)

    def clear_data(self):
        self.data_row = [None]*len(self.header)
        self.start_time = None
        self.diaper_type = None
        self.pee_amount = None
        self.poo_amount = None
        self.blowout = None
        self.color = None

    def write_data(self, data):
        with open(self.data_path, mode='a', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(data)
            
    def publish_data(self):
        if self.start_time is None or self.diaper_type is None:
            return 0
        
        if len(self.data_list) == 0:
            self.write_data(self.header)
        
        self.data_row[self.header.index('diaper_time')] = self.start_time
        self.data_row[self.header.index('diaper_type')] = self.diaper_type
        self.data_row[self.header.index('pee_amount')] = self.pee_amount
        self.data_row[self.header.index('poo_amount')] = self.poo_amount
        self.data_row[self.header.index('blowout')] = self.blowout
        self.data_row[self.header.index('color')] = self.color
        print("Diaper debug data row: ")
        print(self.data_row)
        if None not in self.data_row:
            # publish
            print("Publishing data to " + self.file_name)
            print(self.data_row)
            self.write_data(self.data_row)
            self.clear_data()
            print("Data Cleared")
            print(self.data_row)
            # reset
        else:
            # error
            print("error")
            print(self.data_row)

