#!/usr/bin/env python3
import sys   
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QSpinBox
from PyQt6.QtCore import Qt

class BabyGui(QWidget):
        def __init__(self, state):
            super().__init__()
            
            self.state = state

