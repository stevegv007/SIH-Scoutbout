import csv
import os

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton
)


class LoginWindow:

    def __init__(self):

        # -------------------------------------------------
        # Create the login window
        # -------------------------------------------------

        self.window = QWidget()

        self.window.setWindowTitle("ScoutBot Login")
        self.window.resize(400, 250)

        # False = user has not logged in yet
        # True = user has successfully logged in
        self.login_successful = False


        # -------------------------------------------------
        # Create the layout
        # -------------------------------------------------

        layout = QVBoxLayout()


        # -------------------------------------------------
        # Title
        # -------------------------------------------------

        title = QLabel("ScoutBot Login")

        layout.addWidget(title)


        # -------------------------------------------------
        # Username
        # -------------------------------------------------

        username_label = QLabel("Username:")

        self.username_input = QLineEdit()

        self.username_input.setPlaceholderText(
            "Enter username(all small)"
        )

        layout.addWidget(username_label)
        layout.addWidget(self.username_input)


        # -------------------------------------------------
        # Password
        # -------------------------------------------------

        password_label = QLabel("Password:")

        self.password_input = QLineEdit()

        # Hide the password characters
        self.password_input.setEchoMode(
            QLineEdit.EchoMode.Password
        )

        self.password_input.setPlaceholderText(
            "Enter password"
        )

        layout.addWidget(password_label)
        layout.addWidget(self.password_input)


        # -------------------------------------------------
        # Login button
        # -------------------------------------------------

        self.login_button = QPushButton("Login")

        layout.addWidget(self.login_button)


        # -------------------------------------------------
        # Status message
        # -------------------------------------------------

        self.status_label = QLabel("")

        layout.addWidget(self.status_label)


        # Put the layout into the window
        self.window.setLayout(layout)


        # -------------------------------------------------
        # Connect login button
        # -------------------------------------------------

        self.login_button.clicked.connect(
            self.check_login
        )


    # -----------------------------------------------------
    # Check username and password
    # -----------------------------------------------------

    def check_login(self):

        username = self.username_input.text()
        password = self.password_input.text()

        print("Login button clicked!")
        print("Username:", username)
        print("Password entered:", password)

        if self.check_credentials(username, password):

            print("CREDENTIALS CORRECT!")

            self.login_successful = True

            print("login_successful is now:", self.login_successful)

            self.status_label.setText(
                "Login successful!"
            )

            self.window.close()

        else:

            print("CREDENTIALS WRONG!")

            self.status_label.setText(
                "Incorrect username or password."
            )

            self.password_input.clear()

    # -----------------------------------------------------
    # Read credentials from CSV
    # -----------------------------------------------------

    def check_credentials(self, username, password):

        # Find the folder containing Login.py
        folder = os.path.dirname(
            os.path.abspath(__file__)
        )

        # Find the credentials CSV
        credentials_file = os.path.join(
            folder,
            "Login_Credentials.csv"
        )


        # Open the CSV file
        with open(
            credentials_file,
            "r",
            newline="",
            encoding="utf-8"
        ) as file:

            reader = csv.DictReader(file)

            # Check every account in the CSV
            for row in reader:

                if (
                    row["username"] == username
                    and row["password"] == password
                ):
                    return True

        return False