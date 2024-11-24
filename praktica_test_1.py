from PySide6 import QtWidgets

# app = QtWidgets.QApplication()
#
# window = QtWidgets.QWidget()
# window.setWindowTitle("Простейшее окно")
# window.show()
#
# app.exec()


class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setWindowTitle("Простейшее окно")


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = MyWindow()
    window.show()  # Показ окна

    app.exec()