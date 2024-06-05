import PyQt6.QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QGroupBox, QDialog
from PyQt6.QtWidgets import QTableWidget, QHBoxLayout, QCalendarWidget, QTextBrowser, QLineEdit, QMessageBox
from PyQt6.QtWidgets import QFormLayout, QComboBox, QDialogButtonBox, QLabel, QGridLayout, QTableWidgetItem, QDateEdit
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt


class eventManager(QMainWindow):
    def __init__(self):
        super().__init__()
