import sys
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton
from PyQt5.QtGui import QIcon
class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 örnek window'
        self.left = 60
        self.top =  70
        self.width = 320
        self.height = 240
        self.initUI()
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.button = QPushButton("Tıkla",self)
        self.button.clicked.connect(self.tiklandi)
        self.button.move(10,20)
        self.show()

    def tiklandi(self):
        print("Tıklandı")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
