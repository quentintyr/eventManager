from PyQt6 import QtWidgets, uic
from PyQt6.QtGui import QIcon
from PyQt6 import QtCore

class mainUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(mainUI, self).__init__()   # call the inherited classes __init__ method
        uic.loadUi('ui/eventManager.ui', self)   # load the ui file

        # import css file for stylesheet
        # sshFile = "css/light.qss"
        # with open(sshFile, "r") as fh:
        #     self.setStyleSheet(fh.read())

        # main window settings
        self.setWindowTitle("Event Manager")
        self.setWindowIcon(QIcon("icons/event.png"))
        

        