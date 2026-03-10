#!/usr/bin/env python3
#codebase
import sys   
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QSpinBox, QLabel
from PyQt6.QtCore import Qt

class FeedGui(QWidget):
        def __init__(self, state):
            super().__init__()      
            self.state = state

            self.setWindowTitle("Baby Tracker")
            self.setGeometry(500, 300, 300, 200)
            layout = QVBoxLayout()

            # Headline
            headline = QLabel("Feeder Tracker")
            headline.setAlignment(Qt.AlignmentFlag.AlignCenter)
            headline_font = headline.font()
            headline_font.setPointSize(16)
            headline_font.setBold(True)
            headline.setFont(headline_font)
            layout.addWidget(headline)

            # Start/End Feed Button
            self.time_button = QPushButton("Start Feed Time")
            self.time_button.setStyleSheet("background-color: green")
            self.time_button.clicked.connect(self.on_time_button_clicked)
            layout.addWidget(self.time_button)

            # Counter Button, how many times position switched
            self.counter_button = QPushButton("Click when boob change")
            self.counter_button.clicked.connect(self.on_counter_button_clicked)
            layout.addWidget(self.counter_button)

            # Counter Display Label
            self.counter_label = QLabel("Counter: 0")
            layout.addWidget(self.counter_label)

            # Toggle Breast Button
            self.toggle_button = QPushButton("Started Right ->")
            self.toggle_button.clicked.connect(self.on_toggle_button_clicked)
            layout.addWidget(self.toggle_button)

            # Feed Quality/Strength Label and Spin Box
            quality_label = QLabel("Feed Quality/Strength [1-10]")
            layout.addWidget(quality_label)

            self.selector = QSpinBox()
            self.selector.setRange(1, 10)
            self.selector.setValue(5)
            self.selector.valueChanged.connect(self.state.set_number)
            layout.addWidget(self.selector)

            # Button to publish feed data to log
            self.publish_button = QPushButton("Publish Feed Data")
            self.publish_button.clicked.connect(self.on_publish_button_clicked)
            self.publish_button.setEnabled(False)
            layout.addWidget(self.publish_button)
            
            self.setLayout(layout)

        def on_time_button_clicked(self):
            self.state.record_time()
            if self.state.start_time is not None and self.state.end_time is None:
                self.time_button.setText("End Feed Time")
                self.time_button.setStyleSheet("background-color: red")
            elif self.state.end_time is not None:
                self.publish_button.setEnabled(True)

        def on_counter_button_clicked(self):
            self.state.increment_counter()
            self.counter_label.setText(f"Counter: {self.state.counter}")

        def on_toggle_button_clicked(self):
            self.state.toggle_value()
            if self.state.toggle == 0:
                self.toggle_button.setText("Started Left <-")
            else:
                self.toggle_button.setText("Started Right ->")

        def on_publish_button_clicked(self):
            self.state.publish_data()
            self.time_button.setText("Start Feed Time")
            self.time_button.setStyleSheet("background-color: green")
            self.counter_label.setText("Counter: 0")
            self.publish_button.setEnabled(False)