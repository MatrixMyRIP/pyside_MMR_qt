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

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.settings = QtCore.QSettings("MyMusic")
        self.initSignals()
        self.ui.dial.keyPressEvent = self.ValueEvent

    def initSignals(self) -> None:
        self.ui.dial.valueChanged.connect(self.value_all)
        self.ui.horizontalSlider.valueChanged.connect(self.value_all)
        self.ui.lcdNumber.display(self.value_all())


    def value_all(self):
        value = self.ui.dial.value()
        self.ui.horizontalSlider.setValue(value)
        self.ui.lcdNumber.display(value)


    def ValueEvent(self, event):
         if event.key() == Qt.Key_Plus:
             self.ui.dial.setValue(self.ui.dial.value() + 1)
         elif event.key() == Qt.Key_Minus:
             self.ui.dial.setValue(self.ui.dial.value() - 1)
         else:
             self.keyPressEvent()











if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
