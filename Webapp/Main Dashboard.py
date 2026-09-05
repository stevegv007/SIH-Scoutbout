import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel

def pressed():
    print("Button clicked!")

#Creates the Qt application and starts managing GUI events
app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("My PySide6 App")
window.resize(400, 300)


button = QPushButton("Click Me Brotha", window)
button.move(150, 130)


layout = QHBoxLayout()
label = QLabel("yoooooo")
layout.addWidget(label)
layout.addWidget(button)

window.setLayout(layout)

button.clicked.connect(pressed)

window.show()

sys.exit(app.exec())