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

from ui.system_info import Ui_Form
from a_threads import SystemInfo


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

    def initThreads(self) -> None:
        self.thread = SystemInfo()
        self.thread.systemInfoReceived.connect(self.checkCPU)
        self.thread.systemInfoReceived.connect(self.checkRAM)
        self.thread.start()

    def checkCPU(self, cpu_value) -> None:
        self.ui.CPULabel.setText(f"CPU usage: {cpu_value} %")

    def checkRAM(self, ram_value) -> None:
        self.ui.RAMLabel.setText(f"RAM usage: {ram_value} %")














if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
