import sys

from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout
)

from PySide6.QtCore import QEventLoop, QTimer

# User-made files
from Webapp_Buttons import WebappButton
from Webapp_Labels import WebappLabel
from Webapp_Video import WebappVideo
from Login import LoginWindow


# =================================================
# APPLICATION
# =================================================

app = QApplication(sys.argv)


# =================================================
# LOGIN
# =================================================

login = LoginWindow()

login.window.show()


# =================================================
# WAIT FOR LOGIN
# =================================================

login_loop = QEventLoop()


def check_login():
    # Login was successful
    if login.login_successful:

        print("Login successful!")
        print("Starting dashboard...")

        login_timer.stop()
        login_loop.quit()

    # User closed the login window without logging in
    elif not login.window.isVisible():

        print("Login window closed.")

        login_timer.stop()
        login_loop.quit()


# Check the login status every 100 milliseconds
login_timer = QTimer()

login_timer.timeout.connect(check_login)

login_timer.start(100)


# Run the login event loop
login_loop.exec()


# =================================================
# CHECK RESULT
# =================================================

if not login.login_successful:

    print("Login failed or login window was closed.")
    sys.exit()


# =================================================
# DASHBOARD
# =================================================

window = QWidget()

window.setWindowTitle("My Webapp Dashboard")
window.resize(600, 400)

window.setStyleSheet("""
    QWidget {
        background-color: lightblue;
    }
""")


# =================================================
# MAIN LAYOUT
# =================================================

main_layout = QVBoxLayout()


# =================================================
# WELCOME SECTION
# =================================================

welcome_label = WebappLabel(
    "Welcome to the Dashboard!"
)

main_layout.addWidget(welcome_label.label)


# =================================================
# VIDEO SECTION
# =================================================

video = WebappVideo()

main_layout.addWidget(video.video_widget)


# =================================================
# SAY HELLO SECTION
# =================================================

hello_layout = QHBoxLayout()

hello_label = WebappLabel(
    "Click the button to display a friendly message."
)

hello_button = WebappButton("Say Hello")

hello_layout.addWidget(hello_label.label)
hello_layout.addWidget(hello_button.button)

main_layout.addLayout(hello_layout)


# =================================================
# EXIT SECTION
# =================================================

exit_layout = QHBoxLayout()

exit_label = WebappLabel(
    "Click the button to close the application."
)

exit_button = WebappButton("Exit")

exit_layout.addWidget(exit_label.label)
exit_layout.addWidget(exit_button.button)

main_layout.addLayout(exit_layout)


# =================================================
# BUTTON FUNCTIONS
# =================================================

def say_hello():
    welcome_label.label.setText(
        "Hello! 👋 hope you're fine"
    )


def exit_application():
    app.quit()


# Connect buttons
hello_button.button.clicked.connect(say_hello)
exit_button.button.clicked.connect(exit_application)


# =================================================
# SET DASHBOARD LAYOUT
# =================================================

window.setLayout(main_layout)


# =================================================
# SHOW DASHBOARD
# =================================================

window.show()


# =================================================
# START MAIN APPLICATION
# =================================================

sys.exit(app.exec())