# This Python file uses the following encoding: utf-8
import sys
import requests
import json

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.loginButton.clicked.connect(self.login)

    def login(self):
        email = self.ui.email.toPlainText()
        password = self.ui.password.toPlainText()
        try:
            response = requests.post(
                "http://127.0.0.1:8000/login",
                json={"email": email, "password": password}
            )
            if response.status_code == 200:
                data = response.json()
                QMessageBox.information(self, "Success", f"Welcome: {data['email']}!")
            else:
                QMessageBox.warning(self, "Error", "Invalid credentials. Please try again")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Failed to connect to server: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
