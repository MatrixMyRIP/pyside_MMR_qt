"""
Реализовать окно, которое будет объединять в себе сразу два предыдущих виджета
"""
from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow

from Lab3.b_systeminfo_widget import SistemWindow
from Lab3.c_weatherapi_widget import WeatherWindow
from ui.ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.widget = SistemWindow()
        self.ui.widget_2 = WeatherWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = MainWindow()
    window.show()

    app.exec()
