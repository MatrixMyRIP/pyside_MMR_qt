"""
Реализация программу взаимодействия виджетов друг с другом:
Форма для приложения (ui/d_eventfilter_settings_form.ui)

Программа должна обладать следующим функционалом:

1. Добавить для dial возможность установки значений кнопками клавиатуры(+ и -),
   выводить новые значения в консоль

2. Соединить между собой QDial, QSlider, QLCDNumber
   (изменение значения в одном, изменяет значения в других)

3. Для QLCDNumber сделать отображение в различных системах счисления (oct, hex, bin, dec),
   изменять формат отображаемого значения в зависимости от выбранного в comboBox параметра.

4. Сохранять значение выбранного в comboBox режима отображения
   и значение LCDNumber в QSettings, при перезапуске программы выводить
   в него соответствующие значения
"""

from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtCore import Qt


from ui.d_eventfilter_settings_form import Ui_Form


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.lcd_modes = {
            "hex": QtWidgets.QLCDNumber.Mode.Hex,
            "oct": QtWidgets.QLCDNumber.Mode.Oct,
            "bin": QtWidgets.QLCDNumber.Mode.Bin,
            "dec": QtWidgets.QLCDNumber.Mode.Dec
        }

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.settings = QtCore.QSettings("MyMusic")
        self.initSignals()
        self.ui.comboBox.addItems(list(self.lcd_modes.keys()))
        self.ui.comboBox.currentTextChanged.connect(self.lcd_mode)

        self.ui.comboBox.setCurrentText(self.settings.value("DispMode", "bin"))
        self.ui.lcdNumber.display(self.settings.value("lcdNumber", 0))



    def initSignals(self):
        self.ui.dial.valueChanged.connect(self.value_all)
        self.ui.horizontalSlider.valueChanged.connect(self.value_all)

    def value_all(self, value):
        self.ui.dial.setValue(value)
        self.ui.horizontalSlider.setValue(value)
        self.ui.lcdNumber.display(value)
        self.settings.setValue("lcdNumber", value)
        print(value)

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_Plus:
            self.ui.dial.setValue(self.ui.dial.value() + 1)
        elif key == Qt.Key_Minus:
            self.ui.dial.setValue(self.ui.dial.value() - 1)
        else:
            return

    def lcd_mode(self, mode):
        self.ui.lcdNumber.setMode(self.lcd_modes[mode])
        self.settings.setValue("DispMode", mode)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
