from PySide6.QtWidgets import QApplication, QWidget
from controllers.main_window import ListUserWindow
from PyQt5.QtWidgets import  *
import sys
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ListUserWindow()
    window.show()

    sys.exit(app.exec_())