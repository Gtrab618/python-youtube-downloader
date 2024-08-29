import sys
from PySide6.QtWidgets import QApplication

from Controller.viewController import viewController
from view.viewDonwloader import viewDonwloader

if __name__ == "__main__":
    app = QApplication([])
    window = viewDonwloader()
    controller = viewController(window)
    window.show()
    sys.exit(app.exec())