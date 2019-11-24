from PyQt5.QtWidgets import QApplication,QMainWindow,QLineEdit
from PyQt5 import uic
from DB import DB

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.win = uic.loadUi("veri1.ui")
        self.win.btGonder.clicked.connect(self.kaydet)
        #### Bu kısım düğmeye fonksiyonun atanacağı kısım
        self.win.show()

    def kaydet(self):
        yazi = self.win.txtAd.text()
        db = DB()
        if db.ekleme(yazi) :
            self.win.lblSonuc.setText("Al rite")
        else:
            self.win.lblSonuc.setText("Nope")
        # veri tabanı fonksiyonu üzerinden txt içine yazılmış 
        # verinin kaydedilmesi
        # olumlu yanıtın ekrana yansıtılması

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())