import sys
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton,QLineEdit
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

        self.button = QPushButton("BT 1",self)
        self.button.clicked.connect(self.tiklandi)
        self.button.move(10,20)
        
        self.button1 = QPushButton("BT 2",self)
        self.button1.clicked.connect(self.tiklandi)
        self.button1.move(10,40)

        self.button2 = QPushButton("BT 3",self)
        self.button2.clicked.connect(self.tiklandi)
        self.button2.move(10,60)

        self.txtBox = QLineEdit(self)
        self.txtBox.move(10,80)

        self.show()

    def tiklandi(self):
        print("Tıklandı ",self.sender().text())
    
    def textControl(self):
        girilen = self.txtBox.text()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
