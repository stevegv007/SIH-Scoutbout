import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout, QGridLayout,
    QProgressBar, QFrame
)
from PySide6.QtCore import Qt


class ScoutBotDashboard(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ScoutBot Dashboard")
        self.setMinimumSize(1000, 650)

        self.create_ui()

    def create_ui(self):

        # =========================
        # HEADER
        # =========================

        title = QLabel("🤖 SCOUTBOT")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
            font-size: 28px;
            font-weight: bold;
            padding: 15px;
        """)

        status = QLabel("● CONNECTED")
        status.setAlignment(Qt.AlignCenter)
        status.setStyleSheet("""
            font-size: 16px;
            font-weight: bold;
        """)

        # =========================
        # CAMERA FEED
        # =========================

        camera = QLabel("📹\n\nLIVE CAMERA FEED")
        camera.setAlignment(Qt.AlignCenter)
        camera.setMinimumSize(550, 350)

        camera.setStyleSheet("""
            border: 2px solid gray;
            border-radius: 10px;
            font-size: 22px;
        """)

        # =========================
        # MOVEMENT CONTROLS
        # =========================

        control_title = QLabel("🎮 MOVEMENT CONTROL")
        control_title.setAlignment(Qt.AlignCenter)
        control_title.setStyleSheet("""
            font-size: 18px;
            font-weight: bold;
        """)

        forward = QPushButton("↑\nForward")
        left = QPushButton("←\nLeft")
        stop = QPushButton("⏹\nSTOP")
        right = QPushButton("→\nRight")
        backward = QPushButton("↓\nBackward")

        buttons = [forward, left, stop, right, backward]

        for button in buttons:
            button.setMinimumSize(100, 60)
            button.setStyleSheet("""
                QPushButton {
                    font-size: 15px;
                    font-weight: bold;
                    border: 1px solid gray;
                    border-radius: 8px;
                    padding: 8px;
                }

                QPushButton:hover {
                    background-color: lightgray;
                }
            """)

        # Button positions
        controls = QGridLayout()

        controls.addWidget(forward, 0, 1)
        controls.addWidget(left, 1, 0)
        controls.addWidget(stop, 1, 1)
        controls.addWidget(right, 1, 2)
        controls.addWidget(backward, 2, 1)

        # =========================
        # SENSOR PANEL
        # =========================

        sensor_title = QLabel("📊 SENSOR DATA")
        sensor_title.setStyleSheet("""
            font-size: 18px;
            font-weight: bold;
        """)

        distance = QLabel("Distance: 120 cm")
        temperature = QLabel("Temperature: 28 °C")
        obstacle = QLabel("Obstacle: None")

        for label in [distance, temperature, obstacle]:
            label.setStyleSheet("""
                font-size: 15px;
                padding: 8px;
            """)

        # =========================
        # BATTERY
        # =========================

        battery_title = QLabel("🔋 Battery")

        battery = QProgressBar()
        battery.setValue(78)
        battery.setFormat("78%")

        # =========================
        # ALERT
        # =========================

        alert = QLabel("🚨 Alert: No obstacles detected")
        alert.setWordWrap(True)
        alert.setStyleSheet("""
            border: 1px solid gray;
            border-radius: 6px;
            padding: 10px;
            font-weight: bold;
        """)

        # =========================
        # RIGHT PANEL
        # =========================

        right_panel = QVBoxLayout()

        right_panel.addWidget(control_title)
        right_panel.addLayout(controls)

        right_panel.addSpacing(15)

        right_panel.addWidget(sensor_title)
        right_panel.addWidget(distance)
        right_panel.addWidget(temperature)
        right_panel.addWidget(obstacle)

        right_panel.addSpacing(15)

        right_panel.addWidget(battery_title)
        right_panel.addWidget(battery)

        right_panel.addSpacing(15)

        right_panel.addWidget(alert)

        # =========================
        # MAIN LAYOUT
        # =========================

        main_layout = QVBoxLayout()

        main_layout.addWidget(title)
        main_layout.addWidget(status)

        content = QHBoxLayout()

        content.addWidget(camera)
        content.addLayout(right_panel)

        main_layout.addLayout(content)

        self.setLayout(main_layout)


# =========================
# RUN APPLICATION
# =========================

app = QApplication(sys.argv)

window = ScoutBotDashboard()
window.show()

sys.exit(app.exec())