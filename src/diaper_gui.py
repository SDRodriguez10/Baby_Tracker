#!/usr/bin/env python3
#codebase
import sys   
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QSpinBox, QLabel
from PyQt6.QtCore import Qt

class DiaperGui(QWidget):
        def __init__(self, state):
            super().__init__()      
            self.state = state

            self.setWindowTitle("Baby Tracker")
            self.setGeometry(100, 100, 300, 400)
            layout = QVBoxLayout()

            # Headline
            headline = QLabel("Diaper Tracker")
            headline.setAlignment(Qt.AlignmentFlag.AlignCenter)
            headline_font = headline.font()
            headline_font.setPointSize(16)
            headline_font.setBold(True)
            headline.setFont(headline_font)
            layout.addWidget(headline)

            # Record Diaper Time Button
            self.time_button = QPushButton("Record Diaper Time")
            self.time_button.setStyleSheet("background-color: green")
            self.time_button.clicked.connect(self.on_time_button_clicked)
            layout.addWidget(self.time_button)

            # Diaper Type Selection (3 circle buttons)
            type_label = QLabel("Diaper Type")
            layout.addWidget(type_label)

            self.type_buttons = {}
            diaper_types = ["pee", "poo", "both"]
            for dtype in diaper_types:
                btn = QPushButton(dtype.capitalize())
                btn.clicked.connect(lambda checked, t=dtype: self.on_diaper_type_clicked(t))
                self.type_buttons[dtype] = btn
                layout.addWidget(btn)

            # Pee Amount Label and Spin Box
            self.pee_label = QLabel("Pee Amount")
            self.pee_label.hide()
            layout.addWidget(self.pee_label)

            self.pee_spinbox = QSpinBox()
            self.pee_spinbox.setRange(1, 5)
            self.pee_spinbox.setValue(3)
            self.pee_spinbox.hide()
            layout.addWidget(self.pee_spinbox)

            # Poo Amount Label and Spin Box
            self.poo_label = QLabel("Poo Amount")
            self.poo_label.hide()
            layout.addWidget(self.poo_label)

            self.poo_spinbox = QSpinBox()
            self.poo_spinbox.setRange(1, 5)
            self.poo_spinbox.setValue(3)
            self.poo_spinbox.hide()
            layout.addWidget(self.poo_spinbox)

            # Blowout Button
            self.blowout_button = QPushButton("Blowout: No")
            self.blowout_button.setStyleSheet("background-color: lightgray")
            self.blowout_button.clicked.connect(self.on_blowout_clicked)
            self.blowout = False
            layout.addWidget(self.blowout_button)

            # Color Selection Label and Spin Box
            color_label = QLabel("Color (1-5): yellow, brown, green, black, white")
            layout.addWidget(color_label)

            self.color_spinbox = QSpinBox()
            self.color_spinbox.setRange(1, 5)
            self.color_spinbox.setValue(3)
            layout.addWidget(self.color_spinbox)

            # Publish Button
            self.publish_button = QPushButton("Publish Diaper Data")
            self.publish_button.clicked.connect(self.on_publish_button_clicked)
            self.publish_button.setEnabled(False)
            layout.addWidget(self.publish_button)
            
            self.setLayout(layout)

        def on_time_button_clicked(self):
            self.state.record_time()
            self.publish_button.setEnabled(True)

        def on_diaper_type_clicked(self, diaper_type):
            # Reset all buttons
            for btn in self.type_buttons.values():
                btn.setStyleSheet("")
            # Highlight selected button
            self.type_buttons[diaper_type].setStyleSheet("background-color: lightblue")
            self.selected_diaper_type = diaper_type
            
            # Show/hide spinboxes based on diaper type
            if diaper_type == "pee":
                self.pee_label.show()
                self.pee_spinbox.show()
                self.poo_label.hide()
                self.poo_spinbox.hide()
            elif diaper_type == "poo":
                self.pee_label.hide()
                self.pee_spinbox.hide()
                self.poo_label.show()
                self.poo_spinbox.show()
            elif diaper_type == "both":
                self.pee_label.show()
                self.pee_spinbox.show()
                self.poo_label.show()
                self.poo_spinbox.show()

        def on_blowout_clicked(self):
            self.blowout = not self.blowout
            if self.blowout:
                self.blowout_button.setText("Blowout: Yes")
                self.blowout_button.setStyleSheet("background-color: orange")
            else:
                self.blowout_button.setText("Blowout: No")
                self.blowout_button.setStyleSheet("background-color: lightgray")

        def on_publish_button_clicked(self):
            self.state.publish_data()
            self.time_button.setText("Record Diaper Time")
            self.time_button.setStyleSheet("background-color: green")
            self.pee_spinbox.setValue(3)
            self.poo_spinbox.setValue(3)
            self.color_spinbox.setValue(3)
            self.blowout = False
            self.blowout_button.setText("Blowout: No")
            self.blowout_button.setStyleSheet("background-color: lightgray")
            for btn in self.type_buttons.values():
                btn.setStyleSheet("")
            self.publish_button.setEnabled(False)
