import sys
from PyQt5.QtWidgets import QApplication, QLabel

if __name__ == "__main__":
    app = QApplication([]) #实例化一个QApplication对象用于接收一个列表的值，如果需要传入命令行参数可以传入sys.argv
    label = QLabel('Hello, PyQt!')
    label.show()
    sys.exit(app.exec_())
