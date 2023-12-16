import requests
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem
from ui.main_form_ui import Ui_MainWindow as Ui_MainForm


class MainForm(QMainWindow, Ui_MainForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def set_user_data(self, user_id: int, user_post: int):
        self.user_id = user_id
        self.user_post = user_post
        self.show()

    def get_med(self):
        respons = requests.get("http://127.0.0.1:8000/product")
        medicines = respons.json()['lst']
        self.tableWidget.setRowCount(0)
        row = 0
        for medicine in medicines:
            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row, 0, QTableWidgetItem(medicine.get('title')))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(medicine.get('price')))
            self.tableWidget.resizeColumnsToContents()
            self.tableWidget.horizontalHeader().setStretchLastSection(True)
            row += 1
