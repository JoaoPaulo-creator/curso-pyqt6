from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 800)
        self.setWindowTitle("Curso pyqt6")
        self.setWindowIcon(QIcon('python.png'))
        self.setWindowOpacity(1.9)

app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())
