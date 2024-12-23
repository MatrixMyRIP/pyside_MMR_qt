"""
Реализовать виджет, который будет работать с потоком WeatherHandler из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода широты и долготы (после запуска потока они должны блокироваться)
2. поле для ввода времени задержки (после запуска потока оно должно блокироваться)
3. поле для вывода информации о погоде в указанных координатах
4. поток необходимо запускать и останавливать при нажатии на кнопку
"""
import time

from PySide6 import QtWidgets

from ui.ui_weather import Ui_Form
from a_threads import WeatherHandler


class WeatherWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initSignals()

    def initSignals(self):
        self.ui.start_stop_Button.clicked.connect(self.buttonThread)


    def buttonThread(self, status):
        lat = float(self.ui.line_latedit.text())
        lon = float(self.ui.line_lonedit.text())
        delay = int(self.ui.lineEditDelay.text())
        self.enable_lineedit()
        self.ui.start_stop_Button.setText("Остановить" if status else "Определить")

        if not status:
            self.weather_thread.terminate()
            self.weather_thread.wait(0.5)
            return
        self.weather_thread = WeatherHandler(lat, lon)
        self.weather_thread.setDelay(delay)
        self.weather_thread.start()
        self.weather_thread.weather_signal.connect(self.print_data)

    def print_data(self, text):
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit.appendPlainText(f'{text}\n---\n')

    def enable_lineedit(self):
        if self.ui.start_stop_Button.isChecked():
            self.ui.line_latedit.setEnabled(False)
            self.ui.line_lonedit.setEnabled(False)
            self.ui.lineEditDelay.setEnabled(False)
        elif not self.ui.start_stop_Button.isChecked():
            self.ui.line_latedit.setEnabled(True)
            self.ui.line_lonedit.setEnabled(True)
            self.ui.lineEditDelay.setEnabled(True)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = WeatherWindow()
    window.show()

    app.exec()
