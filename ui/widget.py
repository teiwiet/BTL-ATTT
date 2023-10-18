from PySide6.QtWidgets import QWidget,QDialog
from ui_widget import Ui_Widget
from port_scanner_dialog import PortScannerDialog
class Widget(QWidget,Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Bài tập lớn nhóm ")

        self.port_scanner_button.clicked.connect(self.port_scanner_clicked)
    
        self.port_scanner1 = PortScannerDialog()
    def port_scanner_clicked(self):
        ret = self.port_scanner1.exec()
        if ret == QDialog.Accepted:
            pass