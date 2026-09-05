from PySide6.QtWidgets import QPushButton


class WebappButton:

    def __init__(self, text):
        self.button = QPushButton(text)

    #set_text updates and puts new text
    def set_text(self, text):
        self.button.setText(text)

    #get_text tells you the text being used
    def get_text(self):
        return self.button.text()