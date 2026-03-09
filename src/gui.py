#!/usr/bin/env python3
import sys   
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QSpinBox
from PyQt6.QtCore import Qt

class BabyGui(QWidget):
        def __init__(self, state):
            super().__init__()      
            self.state = state

            self.setWindowTitle("Baby Tracker")
            self.setGeometry(100, 100, 300, 200)
            layout = QVBoxLayout()

            # Start/End Feed Button
            self.time_button = QPushButton("Start/End Feed")
            self.time_button.clicked.connect(self.state.record_time)
            layout.addWidget(self.time_button)

            # COunter Button
            self.counter_button = QPushButton("Increment Counter")
            self.counter_button.clicked.connect(self.state.increment_counter)
            layout.addWidget(self.counter_button)

            # Toggle button
            self.selector = QSpinBox()
            self.selector.setRange(1, 10)
            self.selector.valueChanged.connect(self.state.set_number)
            layout.addWidget(self.selector)

            self.setLayout(layout)