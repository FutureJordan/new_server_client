import sys

import requests
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import pyqtSignal
from PyQt6 import QtWidgets
from src.client.ui.login_form_ui import Ui_MainWindow as Ui_Login_form
from src.client.srck.main_form import MainForm


class LoginForm(QMainWindow, Ui_Login_form):
    login_correct = pyqtSignal(int, int)
    main_form: MainForm

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.button_ToCome.clicked.connect(self.check_login)
        self.button_cancel.clicked.connect(self.exit)

    def check_login(self):
        login = self.line_login.text()
        password = self.line_password.text()

        response = requests.get(f"http://127.0.0.1:8000/login?name={login}&password={password}")
        if response.status_code == 200:
            self.main_form = MainForm()
            self.main_form.set_user_data(user_id=response.json()['id'], user_post='Dolzhnost')
            self.main_form.get_med()
            self.close()

    def exit(self):
        self.close()


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = LoginForm()
    window.show()
    app.exec()

