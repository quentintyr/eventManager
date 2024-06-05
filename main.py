from ui.mainUI import mainUI
from PyQt6.QtWidgets import QApplication


if __name__ == "__main__":
    import sys

    # standard application
    app = QApplication(sys.argv)
    window = mainUI()
    window.show()
    sys.exit(app.exec())

    # sleek light and dark mode
    # app = QApplication(sys.argv)
    # window = mainUI()
    #
    # qtmodern.styles.dark(app)
    # mw = qtmodern.windows.ModernWindow(window)
    # mw.show()
    # sys.exit(app.exec())