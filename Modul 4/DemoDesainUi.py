import sys
from desainUi import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class DemoQtDesainer(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.pushButtonClicked)

    def pushButtonClicked(self):
        QMessageBox.information(self, 'Demo QtDesigner', 'Hallo %s, Apa Kabar ?' % self.ui.lineEdit.text())


if __name__ == "__main__":
    a = QApplication(sys.argv)
    form = DemoQtDesainer()
    form.show()
    a.exec_()