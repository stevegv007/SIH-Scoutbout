from PySide6.QtWidgets import QPushButton


class WebappButton:

    def __init__(self, text):
        self.button = QPushButton(text)

    def set_text(self, text):
        self.button.setText(text)

    def get_text(self):
        return self.button.text()