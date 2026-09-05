from PySide6.QtWidgets import QLabel


class WebappLabel:

    def __init__(self, text):
        self.label = QLabel(text)

    #set_text updates and puts new text
    def set_text(self, text):
        self.label.setText(text)

    #get_text tells you the text being used
    def get_text(self):
        return self.label.text()