import sys
import requests
import json

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox

from ui_form import Ui_MainWindow
from signup import Ui_SignupWindow
from app_window import MainWindow as AppMainWindow


base_url = "http://127.0.0.1:8000"

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.loginButton.clicked.connect(self.login)
        self.ui.signup.clicked.connect(self.signup)

    def login(self):
        email = self.ui.email.toPlainText()
        password = self.ui.password.text()
        try:
            response = requests.post(
                f"{base_url}/token",
                data={"username": email, "password": password}
            )
            if response.status_code == 200:
                data = response.json()
                token = data.get("access_token")
                user_type = data.get("user_type")
                if token:
                    QMessageBox.information(self, "Success", f"Welcome: {email}!")
                    self.app_window = AppMainWindow(token=token, user_type=user_type)
                    self.app_window.show()
                    self.close()

                else:
                    QMessageBox.warning(self, "Error", "Failed to retrieve token. Please try again.")
            else:
                QMessageBox.warning(self, "Error", "Invalid credentials. Please try again.")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Failed to connect to server: {e}")

    def signup(self):
        self.signup_window = SignupWindow()
        self.signup_window.show()


class SignupWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_SignupWindow()
        self.ui.setupUi(self)
        self.ui.signup.clicked.connect(self.signup_handler)

    def signup_handler(self):
        email = self.ui.email.toPlainText()
        first_name = self.ui.first_name.toPlainText()
        last_name = self.ui.last_name.toPlainText()
        password_1 = self.ui.password.text()
        password_2 = self.ui.password_2.text()
        toggled = self.ui.user_type.isChecked()
        json_input = {
            "email": email,
            "password": password_1,
            "first_name": first_name,
            "last_name": last_name,
            "user_type": "standard" if toggled else "moderator"
        }
        if password_1 == password_2:
            try:
                response = requests.post(
                    f"{base_url}/users",
                    json=json_input
                )
                if response.status_code == 200:
                    data = response.json()
                    QMessageBox.information(self, "Sign up successful", f"Welcome: {data['email']}!")
                    self.close()
                elif response.status_code == 400:
                    QMessageBox.warning(self, "Error", "Email already exists")
            except requests.exceptions.RequestException as e:
                QMessageBox.critical(self, "Error", f"Failed to connect to server: {e}")
        else:
            QMessageBox.warning(self, "Error", "Passwords don't match!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = MainWindow()
    login_window.show()
    sys.exit(app.exec())
