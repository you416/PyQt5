# 创建一个PyQt窗口

import sys
from PyQt5.QtWidgets import QApplication, QLabel

if __name__ == "__main__":
    app = QApplication([])
    label = QLabel('Hello, PyQt!')
    label.show()
    sys.exit(app.exec_())
