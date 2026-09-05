import sys

from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout
)

from Webapp_Buttons import WebappButton
from Webapp_Labels import WebappLabel


# Create the application
app = QApplication(sys.argv)


# Create the main window
window = QWidget()
window.setWindowTitle("My Webapp Dashboard")
window.resize(600, 400)


# Main vertical layout
main_layout = QVBoxLayout()


# -------------------------
# Welcome section
# -------------------------

welcome_label = WebappLabel("Welcome to the Dashboard!")

main_layout.addWidget(welcome_label.label)


# -------------------------
# Button 1
# -------------------------

button1_layout = QHBoxLayout()

button1_label = WebappLabel("Click this to display a message.")
button1 = WebappButton("Say Hello")

button1_layout.addWidget(button1_label.label)
button1_layout.addWidget(button1.button)

main_layout.addLayout(button1_layout)


# -------------------------
# Button 2
# -------------------------

button2_layout = QHBoxLayout()

button2_label = WebappLabel("Click this to change the welcome message.")
button2 = WebappButton("Change Title")

button2_layout.addWidget(button2_label.label)
button2_layout.addWidget(button2.button)

main_layout.addLayout(button2_layout)


# -------------------------
# Button 3
# -------------------------

button3_layout = QHBoxLayout()

button3_label = WebappLabel("Click this to close the application.")
button3 = WebappButton("Exit")

button3_layout.addWidget(button3_label.label)
button3_layout.addWidget(button3.button)

main_layout.addLayout(button3_layout)


# -------------------------
# Button functions
# -------------------------

def say_hello():
    welcome_label.label.setText("Hello! 👋")


def change_title():
    welcome_label.label.setText("You changed the dashboard!")


def exit_application():
    app.quit()


# Connect buttons to functions

button1.button.clicked.connect(say_hello)
button2.button.clicked.connect(change_title)
button3.button.clicked.connect(exit_application)


# Give the window its layout
window.setLayout(main_layout)


# Show the window
window.show()


# Start the application
sys.exit(app.exec())