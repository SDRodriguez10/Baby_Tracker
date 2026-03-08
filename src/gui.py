#!/usr/bin/env python3
import sys   
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtCore import Qt

class BabyGui(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Simple PyQt App") # Set the window title
            self.setGeometry(100, 100, 400, 200)   # Set position and size (x, y, width, height) 
            # Create a label widget
            self.label = QLabel("Hello World !!", self)
            self.label.setAlignment(Qt.AlignmentFlag.AlignCenter) # Center the text
            self.setCentralWidget(self.label) # Set the label as the central widget of the window
