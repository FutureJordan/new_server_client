import sys

from PyQt6 import QtWidgets



from srck.login_form import LoginForm
from srck.main_form import MainForm


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    login_window = LoginForm()
    main_form = MainForm()
    login_window.login_correct.connect(main_form.set_user_data)
    login_window.login_correct.connect(main_form.show)
    login_window.show()
    app.exec()







