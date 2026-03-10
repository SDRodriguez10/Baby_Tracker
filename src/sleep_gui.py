#!/usr/bin/env python3
import sys   
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QSpinBox, QLabel
from PyQt6.QtCore import Qt

class SleepGui(QWidget):
        def __init__(self, state):
            super().__init__()      
            self.state = state

            self.setWindowTitle("Baby Tracker")
            self.setGeometry(100, 100, 300, 200)
            layout = QVBoxLayout()

            # Headline
            headline = QLabel("Sleep Tracker")
            headline.setAlignment(Qt.AlignmentFlag.AlignCenter)
            headline_font = headline.font()
            headline_font.setPointSize(16)
            headline_font.setBold(True)
            headline.setFont(headline_font)
            layout.addWidget(headline)

            # Start/End Sleep Button
            self.time_button = QPushButton("Start Sleep Time")
            self.time_button.setStyleSheet("background-color: green")
            self.time_button.clicked.connect(self.on_time_button_clicked)
            layout.addWidget(self.time_button)

            # Sleep Quality Label and Spin Box
            quality_label = QLabel("Sleep Quality")
            layout.addWidget(quality_label)

            self.selector = QSpinBox()
            self.selector.setRange(1, 10)
            self.selector.setValue(5)
            self.selector.valueChanged.connect(self.state.set_number)
            layout.addWidget(self.selector)

            self.publish_button = QPushButton("Publish Sleep Data")
            self.publish_button.clicked.connect(self.on_publish_button_clicked)
            self.publish_button.setEnabled(False)
            layout.addWidget(self.publish_button)
            
            self.setLayout(layout)

        def on_time_button_clicked(self):
            self.state.record_time()
            if self.state.start_time is not None and self.state.end_time is None:
                self.time_button.setText("End Sleep Time")
                self.time_button.setStyleSheet("background-color: red")
            elif self.state.end_time is not None:
                self.publish_button.setEnabled(True)

        def on_publish_button_clicked(self):
            self.state.publish_data()
            self.time_button.setText("Start Sleep Time")
            self.time_button.setStyleSheet("background-color: green")
            self.selector.setValue(5)
            self.publish_button.setEnabled(False)
