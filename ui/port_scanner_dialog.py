from PySide6.QtWidgets import QDialog 
from ui_port_scanner import Ui_port_scanner
import function
class PortScannerDialog(QDialog,Ui_port_scanner):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Port Scanner by nhóm")
        self.start_button.clicked.connect(self.scan)

        self.current = ""
    def scan(self):
        if self.line_edit_1.text() !="":
            self.label.setText("lmao")