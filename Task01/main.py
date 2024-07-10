from PySide6.QtWidgets import QApplication
import sys
from MainWindow import testwidget

app = QApplication(sys.argv)
window = testwidget()


window.show()
app.exec()