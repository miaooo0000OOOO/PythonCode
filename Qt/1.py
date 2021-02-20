import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QIcon

class ChuangKou(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('标题')
        #self.setWindowIcon(QIcon('web.jpg'))
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ChuangKou()
    sys.exit(app.exec_())
