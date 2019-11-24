from PyQt5.QtWidgets import QApplication,QMainWindow,QLineEdit,QMessageBox
from PyQt5 import uic
from DB import DB

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.win = uic.loadUi("veri1.ui")
        self.ilDoldur()
        self.win.btGonder.clicked.connect(self.kaydet)
        self.win.cmbIl.currentIndexChanged.connect(self.tespit)
        self.win.show()

    def kaydet(self):
        adi = self.win.txtAd.text()
        soyadi = self.win.txtSoyad.text()
        il = self.win.cmbIl.currentIndex()
        ilce = self.win.cmbIlce.currentIndex()
        if self.win.rdbKadin.isChecked():
            cinsiyet = 0
        elif self.win.rdbErkek.isChecked():
            cinsiyet = 1
        db = DB()
        if db.ekleme(adi,soyadi,il,ilce,cinsiyet):
            elCevap =  QMessageBox.question(self,"Soru","Kaydetmek İster misin?",\
                QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,\
                    QMessageBox.Yes)
            if elCevap == QMessageBox.Yes:
                QMessageBox.information(self,"Bilgi","Kaydedildi!.")
        else:
            QMessageBox.warning(self,"Hata","Hata Var!.")
    
    def ilDoldur(self):
        db = DB()
        liste  = db.ilListele()
        self.win.cmbIl.addItem("Seçiniz")
        for IlKod,IlAd in liste:
            self.win.cmbIl.addItem(IlAd)
        
    
    def ilceDoldur(self,il="1"):
        db = DB()
        liste  = db.ilceListele(il)
        self.win.cmbIlce.clear()
        self.win.cmbIlce.addItem("Seçiniz")
        for IlceKod,IlceAd in liste:
            self.win.cmbIlce.addItem(IlceAd)


    def tespit(self):
        self.ilceDoldur(str(self.win.cmbIl.currentIndex()))

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())