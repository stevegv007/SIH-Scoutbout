from PySide6.QtWidgets import QPushButton


class WebappButton:

    def __init__(self, text):
        self.button = QPushButton(text)

        # Basic button styling
        #color is for text, bg color is for bg colour, radius is for curvature of button
        #padding idk about
        self.button.setStyleSheet("""
            QPushButton {
                background-color: #4A90E2;
                color: white;
                border-radius: 8px;
                padding: 8px 16px;
                font-size: 14px;
            }

            QPushButton:hover {
                background-color: #357ABD;
            }

            QPushButton:pressed {
                background-color: #286090;
            }
        """)

    def set_text(self, text):
        self.button.setText(text)

    def get_text(self):
        return self.button.text()