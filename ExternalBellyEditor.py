import sys
from PyQt5.QtWidgets import QApplication
from scripts.main import VRDBEditor

if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = VRDBEditor()
    editor.show()
    sys.exit(app.exec_())
