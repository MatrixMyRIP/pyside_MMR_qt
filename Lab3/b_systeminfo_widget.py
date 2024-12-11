"""
Реализовать виджет, который будет работать с потоком SystemInfo из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода времени задержки
2. поле для вывода информации о загрузке CPU
3. поле для вывода информации о загрузке RAM
4. поток необходимо запускать сразу при старте приложения
5. установку времени задержки сделать "горячей", т.е. поток должен сразу
реагировать на изменение времени задержки
"""

from PySide6 import QtWidgets
from PySide6.QtWidgets import QLineEdit
import traceback

from ui.system_info import Ui_Form
from a_threads import SystemInfo


class SistemWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initThreads()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initSignals()

    def initThreads(self) -> None:
        self.thread = SystemInfo()
        self.thread.systemInfoReceived.connect(self.checkUP)
        self.thread.start()

    def initSignals(self) -> None:
        self.ui.DelayLineEdit.textChanged.connect(self.onDelayLineEditTextChanged)

    def checkUP(self, value) -> None:
        self.ui.CPULabel.setText(f"CPU usage: {value} %")
        self.ui.RAMLabel.setText(f"RAM usage: {value} %")

    def onDelayLineEditTextChanged(self, data):
        try:
            delay = int(data)
            self.thread.setDelay(delay)
        except Exception:
            traceback.print_exc()
            pass
        # print(delay)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = SistemWindow()
    window.show()

    app.exec()
