from PySide6.QtWidgets import QApplication,QWidget
from widget import Widget

app = QApplication([])
window = Widget()
window.show()
app.exec()