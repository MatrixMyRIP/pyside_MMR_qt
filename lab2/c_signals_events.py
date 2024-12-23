"""
Реализация программу проверки состояния окна:
Форма для приложения (ui/c_signals_events_form.ui)

Программа должна обладать следующим функционалом:

1. Возможность перемещения окна по заданным координатам.
2. Возможность получения параметров экрана (вывод производить в plainTextEdit + добавлять время).
    * Кол-во экранов
    * Текущее основное окно
    * Разрешение экрана
    * На каком экране окно находится
    * Размеры окна
    * Минимальные размеры окна
    * Текущее положение (координаты) окна
    * Координаты центра приложения
    * Отслеживание состояния окна (свернуто/развёрнуто/активно/отображено)
3. Возможность отслеживания состояния окна (вывод производить в консоль + добавлять время).
    * При перемещении окна выводить его старую и новую позицию
    * При изменении размера окна выводить его новый размер
"""
import time
from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtGui import QGuiApplication
from ui.c_signals_events_form import Ui_Form


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initSignals()

    def initSignals(self):
        self.ui.pushButtonMoveCoords.clicked.connect(self.MoveCoords)
        self.ui.pushButtonGetData.clicked.connect(self.GetDataScreen)

    def MoveCoords(self):
        y = self.ui.spinBoxY.value()
        x = self.ui.spinBoxX.value()
        self.move(x, y)
        self.ui.plainTextEdit.appendPlainText(f"Окно перемещено на координаты {x}, {y}")


    def GetDataScreen(self):
        data = {"Кол-во экранов": QGuiApplication.screens(),
                "Текущее основное окно": self,
                "Разрешение экрана": QGuiApplication.primaryScreen().size(),
                "На каком экране окно находится": self.screen(),
                "Размеры окна": self.size(),
                "Минимальные размеры окна": self.minimumSize(),
                "Текущее положение (координаты) окна": self.geometry(),
                "Координаты центра приложения": self.geometry().center(),
                "Отслеживание состояния окна (свернуто/развёрнуто/активно/отображено)": [self.showWindowState(),
                                                                                         self.showWindowActiv()]
                }

        for key, value in data.items():
            self.ui.plainTextEdit.appendPlainText(f"{key}: {value}")

        self.ui.plainTextEdit.appendPlainText(time.ctime())
        print(data)

    def event(self, event):
        if event.type() == QtCore.QEvent.Type.WindowStateChange:
            self.showWindowState()
            # self.showWindowState_2()
        if event.type() == QtCore.QEvent.Type.ActivationChange:
            self.showWindowActiv()

        return super().event(event)


    def showWindowState(self):
        if self.isHidden():
            return f"свернуто"
        else:
            return f"развёрнуто"

    # def showWindowState_2(self):
    #     if self.isFullScreen():
    #         return f"развёрнуто"
    #     else:
    #         return f"свернуто"     # В этом случае выдает с ошибкой - пишет, что свернуто.

    def showWindowActiv(self):
        if self.isActiveWindow():
            return f"активно"
        else:
            f"отображено"


    def moveEvent(self, event: QtGui.QMoveEvent):
        oldPos = event.oldPos()
        newPos = event.pos()
        self.ui.plainTextEdit.appendPlainText(f"{oldPos}, {newPos}")
        self.ui.plainTextEdit.appendPlainText(time.ctime())

    def resizeEvent(self, event: QtGui.QResizeEvent):
        resize = event.size()
        self.ui.plainTextEdit.appendPlainText(f"{resize}")


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
