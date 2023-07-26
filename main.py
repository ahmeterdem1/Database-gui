import csv, sys, time
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QSlider, QLabel, QStyle, QWidget, \
    QVBoxLayout, QMessageBox, QTabWidget, QComboBox, QHBoxLayout, QLineEdit, QTextEdit
from PySide6.QtCore import QRect, QPoint, Qt, QTime, QSize
from PySide6.QtGui import QScreen

class Widget(QWidget):

    def __init__(self):
        super().__init__()
        self.data = 0
        self.criterias = [None] * 11
        self.result = list()
        with open("database.csv", "r") as file:
            self.data = list(csv.reader(file))

        general_layout = QVBoxLayout()
        tabs = QTabWidget(self)
        #code here

        #filtrele

        filtrele = QWidget()
        filtrele_layout = QVBoxLayout()

        tc_widget = QWidget()
        tc = QHBoxLayout()
        tc1 = QLabel("TC No: ")
        tc2 = QLineEdit()
        self.tc = tc2
        tc.addWidget(tc1)
        tc.addWidget(tc2)
        tc_widget.setLayout(tc)

        isim_widget = QWidget()
        isim = QHBoxLayout()
        isim1 = QLabel("İsim: ")
        isim2 = QLineEdit()
        self.isim = isim2
        isim.addWidget(isim1)
        isim.addWidget(isim2)
        isim_widget.setLayout(isim)

        tc_isim = QWidget()
        tc_isim_layout = QHBoxLayout()
        tc_isim_layout.addWidget(tc_widget)
        tc_isim_layout.addWidget(isim_widget)
        tc_isim.setLayout(tc_isim_layout)

        soyisim_widget = QWidget()
        soyisim = QHBoxLayout()
        soyisim1 = QLabel("Soyisim: ")
        soyisim2 = QLineEdit()
        self.soyisim = soyisim2
        soyisim.addWidget(soyisim1)
        soyisim.addWidget(soyisim2)
        soyisim_widget.setLayout(soyisim)

        yaş_widget = QWidget()
        yaş = QHBoxLayout()
        yaş1 = QLabel("Yaş: ")
        yaş2 = QLineEdit()
        self.yaş = yaş2
        yaş.addWidget(yaş1)
        yaş.addWidget(yaş2)
        yaş_widget.setLayout(yaş)

        soyisim_yaş = QWidget()
        soyisim_yaş_layout = QHBoxLayout()
        soyisim_yaş_layout.addWidget(soyisim_widget)
        soyisim_yaş_layout.addWidget(yaş_widget)
        soyisim_yaş.setLayout(soyisim_yaş_layout)

        telno_widget = QWidget()
        telno = QHBoxLayout()
        telno1 = QLabel("Tel No: ")
        telno2 = QLineEdit()
        self.telno = telno2
        telno.addWidget(telno1)
        telno.addWidget(telno2)
        telno_widget.setLayout(telno)

        adres_widget = QWidget()
        adres = QHBoxLayout()
        adres1 = QLabel("Adres: ")
        adres2 = QLineEdit()
        self.adres = adres2
        adres.addWidget(adres1)
        adres.addWidget(adres2)
        adres_widget.setLayout(adres)

        telno_adres = QWidget()
        telno_adres_layout = QHBoxLayout()
        telno_adres_layout.addWidget(telno_widget)
        telno_adres_layout.addWidget(adres_widget)
        telno_adres.setLayout(telno_adres_layout)

        genel_bölge_widget = QWidget()
        genel_bölge = QHBoxLayout()
        genel_bölge1 = QLabel("Genel Bölge: ")
        genel_bölge2 = QComboBox(self)
        self.genel_bölge = genel_bölge2
        self.genel_bölge.addItem("Hiçbiri")
        self.genel_bölge.addItem("1")
        self.genel_bölge.addItem("2")
        self.genel_bölge.addItem("3")
        self.genel_bölge.addItem("4")
        self.genel_bölge.addItem("5")
        self.genel_bölge.addItem("6")
        self.genel_bölge.addItem("7")
        self.genel_bölge.addItem("8")
        self.genel_bölge.addItem("9")
        self.genel_bölge.addItem("10")
        genel_bölge.addWidget(genel_bölge1)
        genel_bölge.addWidget(genel_bölge2)
        genel_bölge_widget.setLayout(genel_bölge)

        ihtiyaç_sınıfı_widget = QWidget()
        ihtiyaç_sınıfı = QHBoxLayout()
        ihtiyaç_sınıfı1 = QLabel("İhtiyaç sınıfı: ")
        ihtiyaç_sınıfı2 = QComboBox(self)
        self.ihtiyaç_sınıfı = ihtiyaç_sınıfı2
        self.ihtiyaç_sınıfı.addItem("Hiçbiri")
        self.ihtiyaç_sınıfı.addItem("1")
        self.ihtiyaç_sınıfı.addItem("2")
        self.ihtiyaç_sınıfı.addItem("3")
        self.ihtiyaç_sınıfı.addItem("4")
        self.ihtiyaç_sınıfı.addItem("5")
        self.ihtiyaç_sınıfı.addItem("6")
        self.ihtiyaç_sınıfı.addItem("7")
        ihtiyaç_sınıfı.addWidget(ihtiyaç_sınıfı1)
        ihtiyaç_sınıfı.addWidget(ihtiyaç_sınıfı2)
        ihtiyaç_sınıfı_widget.setLayout(ihtiyaç_sınıfı)

        genel_bölge_ihtiyaç_sınıfı = QWidget()
        genel_bölge_ihtiyaç_sınıfı_layout = QHBoxLayout()
        genel_bölge_ihtiyaç_sınıfı_layout.addWidget(genel_bölge_widget)
        genel_bölge_ihtiyaç_sınıfı_layout.addWidget(ihtiyaç_sınıfı_widget)
        genel_bölge_ihtiyaç_sınıfı.setLayout(genel_bölge_ihtiyaç_sınıfı_layout)

        özel_durum_widget = QWidget()
        özel_durum = QHBoxLayout()
        özel_durum1 = QLabel("Özel durum: ")
        özel_durum2 = QComboBox(self)
        self.özel_durum = özel_durum2
        self.özel_durum.addItem("Hiçbiri")
        self.özel_durum.addItem("1")
        self.özel_durum.addItem("2")
        self.özel_durum.addItem("3")
        self.özel_durum.addItem("4")
        self.özel_durum.addItem("5")
        özel_durum.addWidget(özel_durum1)
        özel_durum.addWidget(özel_durum2)
        özel_durum_widget.setLayout(özel_durum)

        ihtiyaç_seviyesi_widget = QWidget()
        ihtiyaç_seviyesi = QHBoxLayout()
        ihtiyaç_seviyesi1 = QLabel("İhtiyaç seviyesi: ")
        ihtiyaç_seviyesi2 = QComboBox(self)
        self.ihtiyaç_seviyesi = ihtiyaç_seviyesi2
        self.ihtiyaç_seviyesi.addItem("Hiçbiri")
        self.ihtiyaç_seviyesi.addItem("1")
        self.ihtiyaç_seviyesi.addItem("2")
        self.ihtiyaç_seviyesi.addItem("3")
        self.ihtiyaç_seviyesi.addItem("4")
        self.ihtiyaç_seviyesi.addItem("5")
        ihtiyaç_seviyesi.addWidget(ihtiyaç_seviyesi1)
        ihtiyaç_seviyesi.addWidget(ihtiyaç_seviyesi2)
        ihtiyaç_seviyesi_widget.setLayout(ihtiyaç_seviyesi)

        özel_durum_ihtiyaç_seviyesi = QWidget()
        özel_durum_ihtiyaç_seviyesi_layout = QHBoxLayout()
        özel_durum_ihtiyaç_seviyesi_layout.addWidget(özel_durum_widget)
        özel_durum_ihtiyaç_seviyesi_layout.addWidget(ihtiyaç_seviyesi_widget)
        özel_durum_ihtiyaç_seviyesi.setLayout(özel_durum_ihtiyaç_seviyesi_layout)

        yardım_widget = QWidget()
        yardım = QHBoxLayout()
        yardım1 = QLabel("Yardım alma durumu: ")
        yardım2 = QComboBox(self)
        self.yardım = yardım2
        self.yardım.addItem("Hiçbiri")
        self.yardım.addItem("Hayır")
        self.yardım.addItem("Evet")
        yardım.addWidget(yardım1)
        yardım.addWidget(yardım2)
        yardım_widget.setLayout(yardım)

        self.ara = QPushButton("Filtrele")
        self.ara.clicked.connect(self.filtrele)

        yardım_filtrele = QWidget()
        yardım_filtrele_layout = QHBoxLayout()
        yardım_filtrele_layout.addWidget(yardım_widget)
        yardım_filtrele_layout.addWidget(self.ara)
        yardım_filtrele.setLayout(yardım_filtrele_layout)

        filtrele_layout.addWidget(tc_isim)
        filtrele_layout.addWidget(soyisim_yaş)
        filtrele_layout.addWidget(telno_adres)
        filtrele_layout.addWidget(genel_bölge_ihtiyaç_sınıfı)
        filtrele_layout.addWidget(özel_durum_ihtiyaç_seviyesi)
        filtrele_layout.addWidget(yardım_filtrele)
        filtrele.setLayout(filtrele_layout)

        #kişi ekle

        ekle = QWidget()
        ekle_layout = QVBoxLayout()

        tc_ekle_widget = QWidget()
        tc_ekle = QHBoxLayout()
        tc1_ekle = QLabel("TC No: ")
        tc2_ekle = QLineEdit()
        self.tc_ekle = tc2_ekle
        tc_ekle.addWidget(tc1_ekle)
        tc_ekle.addWidget(tc2_ekle)
        tc_ekle_widget.setLayout(tc_ekle)

        isim_ekle_widget = QWidget()
        isim_ekle = QHBoxLayout()
        isim1_ekle = QLabel("İsim: ")
        isim2_ekle = QLineEdit()
        self.isim_ekle = isim2_ekle
        isim_ekle.addWidget(isim1_ekle)
        isim_ekle.addWidget(isim2_ekle)
        isim_ekle_widget.setLayout(isim_ekle)

        tc_isim_ekle = QWidget()
        tc_isim_ekle_layout = QHBoxLayout()
        tc_isim_ekle_layout.addWidget(tc_ekle_widget)
        tc_isim_ekle_layout.addWidget(isim_ekle_widget)
        tc_isim_ekle.setLayout(tc_isim_ekle_layout)

        soyisim_ekle_widget = QWidget()
        soyisim_ekle = QHBoxLayout()
        soyisim1_ekle = QLabel("Soyisim: ")
        soyisim2_ekle = QLineEdit()
        self.soyisim_ekle = soyisim2_ekle
        soyisim_ekle.addWidget(soyisim1_ekle)
        soyisim_ekle.addWidget(soyisim2_ekle)
        soyisim_ekle_widget.setLayout(soyisim_ekle)

        yaş_ekle_widget = QWidget()
        yaş_ekle = QHBoxLayout()
        yaş1_ekle = QLabel("Yaş: ")
        yaş2_ekle = QLineEdit()
        self.yaş_ekle = yaş2_ekle
        yaş_ekle.addWidget(yaş1_ekle)
        yaş_ekle.addWidget(yaş2_ekle)
        yaş_ekle_widget.setLayout(yaş_ekle)

        soyisim_yaş_ekle = QWidget()
        soyisim_yaş_ekle_layout = QHBoxLayout()
        soyisim_yaş_ekle_layout.addWidget(soyisim_ekle_widget)
        soyisim_yaş_ekle_layout.addWidget(yaş_ekle_widget)
        soyisim_yaş_ekle.setLayout(soyisim_yaş_ekle_layout)

        telno_ekle_widget = QWidget()
        telno_ekle = QHBoxLayout()
        telno1_ekle = QLabel("Tel No: ")
        telno2_ekle = QLineEdit()
        self.telno_ekle = telno2_ekle
        telno_ekle.addWidget(telno1_ekle)
        telno_ekle.addWidget(telno2_ekle)
        telno_ekle_widget.setLayout(telno_ekle)

        adres_ekle_widget = QWidget()
        adres_ekle = QHBoxLayout()
        adres1_ekle = QLabel("Adres: ")
        adres2_ekle = QLineEdit()
        self.adres_ekle = adres2_ekle
        adres_ekle.addWidget(adres1_ekle)
        adres_ekle.addWidget(adres2_ekle)
        adres_ekle_widget.setLayout(adres_ekle)

        telno_adres_ekle = QWidget()
        telno_adres_ekle_layout = QHBoxLayout()
        telno_adres_ekle_layout.addWidget(telno_ekle_widget)
        telno_adres_ekle_layout.addWidget(adres_ekle_widget)
        telno_adres_ekle.setLayout(telno_adres_ekle_layout)

        genel_bölge_ekle_widget = QWidget()
        genel_bölge_ekle = QHBoxLayout()
        genel_bölge1_ekle = QLabel("Genel Bölge: ")
        genel_bölge2_ekle = QComboBox(self)
        self.genel_bölge_ekle = genel_bölge2_ekle
        self.genel_bölge_ekle.addItem("Hiçbiri")
        self.genel_bölge_ekle.addItem("1")
        self.genel_bölge_ekle.addItem("2")
        self.genel_bölge_ekle.addItem("3")
        self.genel_bölge_ekle.addItem("4")
        self.genel_bölge_ekle.addItem("5")
        self.genel_bölge_ekle.addItem("6")
        self.genel_bölge_ekle.addItem("7")
        self.genel_bölge_ekle.addItem("8")
        self.genel_bölge_ekle.addItem("9")
        self.genel_bölge_ekle.addItem("10")
        genel_bölge_ekle.addWidget(genel_bölge1_ekle)
        genel_bölge_ekle.addWidget(genel_bölge2_ekle)
        genel_bölge_ekle_widget.setLayout(genel_bölge_ekle)

        ihtiyaç_sınıfı_ekle_widget = QWidget()
        ihtiyaç_sınıfı_ekle = QHBoxLayout()
        ihtiyaç_sınıfı1_ekle = QLabel("İhtiyaç sınıfı: ")
        ihtiyaç_sınıfı2_ekle = QComboBox(self)
        self.ihtiyaç_sınıfı_ekle = ihtiyaç_sınıfı2_ekle
        self.ihtiyaç_sınıfı_ekle.addItem("Hiçbiri")
        self.ihtiyaç_sınıfı_ekle.addItem("1")
        self.ihtiyaç_sınıfı_ekle.addItem("2")
        self.ihtiyaç_sınıfı_ekle.addItem("3")
        self.ihtiyaç_sınıfı_ekle.addItem("4")
        self.ihtiyaç_sınıfı_ekle.addItem("5")
        self.ihtiyaç_sınıfı_ekle.addItem("6")
        self.ihtiyaç_sınıfı_ekle.addItem("7")
        ihtiyaç_sınıfı_ekle.addWidget(ihtiyaç_sınıfı1_ekle)
        ihtiyaç_sınıfı_ekle.addWidget(ihtiyaç_sınıfı2_ekle)
        ihtiyaç_sınıfı_ekle_widget.setLayout(ihtiyaç_sınıfı_ekle)

        genel_bölge_ihtiyaç_sınıfı_ekle = QWidget()
        genel_bölge_ihtiyaç_sınıfı_ekle_layout = QHBoxLayout()
        genel_bölge_ihtiyaç_sınıfı_ekle_layout.addWidget(genel_bölge_ekle_widget)
        genel_bölge_ihtiyaç_sınıfı_ekle_layout.addWidget(ihtiyaç_sınıfı_ekle_widget)
        genel_bölge_ihtiyaç_sınıfı_ekle.setLayout(genel_bölge_ihtiyaç_sınıfı_ekle_layout)

        özel_durum_ekle_widget = QWidget()
        özel_durum_ekle = QHBoxLayout()
        özel_durum1_ekle = QLabel("Özel durum: ")
        özel_durum2_ekle = QComboBox(self)
        self.özel_durum_ekle = özel_durum2_ekle
        self.özel_durum_ekle.addItem("Hiçbiri")
        self.özel_durum_ekle.addItem("1")
        self.özel_durum_ekle.addItem("2")
        self.özel_durum_ekle.addItem("3")
        self.özel_durum_ekle.addItem("4")
        self.özel_durum_ekle.addItem("5")
        özel_durum_ekle.addWidget(özel_durum1_ekle)
        özel_durum_ekle.addWidget(özel_durum2_ekle)
        özel_durum_ekle_widget.setLayout(özel_durum_ekle)

        ihtiyaç_seviyesi_ekle_widget = QWidget()
        ihtiyaç_seviyesi_ekle = QHBoxLayout()
        ihtiyaç_seviyesi1_ekle = QLabel("İhtiyaç seviyesi: ")
        ihtiyaç_seviyesi2_ekle = QComboBox(self)
        self.ihtiyaç_seviyesi_ekle = ihtiyaç_seviyesi2_ekle
        self.ihtiyaç_seviyesi_ekle.addItem("Hiçbiri")
        self.ihtiyaç_seviyesi_ekle.addItem("1")
        self.ihtiyaç_seviyesi_ekle.addItem("2")
        self.ihtiyaç_seviyesi_ekle.addItem("3")
        self.ihtiyaç_seviyesi_ekle.addItem("4")
        self.ihtiyaç_seviyesi_ekle.addItem("5")
        ihtiyaç_seviyesi_ekle.addWidget(ihtiyaç_seviyesi1_ekle)
        ihtiyaç_seviyesi_ekle.addWidget(ihtiyaç_seviyesi2_ekle)
        ihtiyaç_seviyesi_ekle_widget.setLayout(ihtiyaç_seviyesi_ekle)

        özel_durum_ihtiyaç_seviyesi_ekle = QWidget()
        özel_durum_ihtiyaç_seviyesi_ekle_layout = QHBoxLayout()
        özel_durum_ihtiyaç_seviyesi_ekle_layout.addWidget(özel_durum_ekle_widget)
        özel_durum_ihtiyaç_seviyesi_ekle_layout.addWidget(ihtiyaç_seviyesi_ekle_widget)
        özel_durum_ihtiyaç_seviyesi_ekle.setLayout(özel_durum_ihtiyaç_seviyesi_ekle_layout)

        yardım_ekle_widget = QWidget()
        yardım_ekle = QHBoxLayout()
        yardım1_ekle = QLabel("Yardım alma durumu: ")
        yardım2_ekle = QComboBox(self)
        self.yardım_ekle = yardım2_ekle
        self.yardım_ekle.addItem("Hiçbiri")
        self.yardım_ekle.addItem("Hayır")
        self.yardım_ekle.addItem("Evet")
        yardım_ekle.addWidget(yardım1_ekle)
        yardım_ekle.addWidget(yardım2_ekle)
        yardım_ekle_widget.setLayout(yardım_ekle)

        self.add = QPushButton("Ekle")
        self.drop = QPushButton("Çıkar")
        self.add.clicked.connect(self.ekle)
        self.drop.clicked.connect(self.çıkar)

        yardım_ekle_çıkar = QWidget()
        yardım_ekle_çıkar_layout = QHBoxLayout()
        yardım_ekle_çıkar_layout.addWidget(yardım_ekle_widget)
        yardım_ekle_çıkar_layout.addWidget(self.add)
        yardım_ekle_çıkar_layout.addWidget(self.drop)
        yardım_ekle_çıkar.setLayout(yardım_ekle_çıkar_layout)

        ekle_layout.addWidget(tc_isim_ekle)
        ekle_layout.addWidget(soyisim_yaş_ekle)
        ekle_layout.addWidget(telno_adres_ekle)
        ekle_layout.addWidget(genel_bölge_ihtiyaç_sınıfı_ekle)
        ekle_layout.addWidget(özel_durum_ihtiyaç_seviyesi_ekle)
        ekle_layout.addWidget(yardım_ekle_çıkar)
        ekle.setLayout(ekle_layout)

        #sonuçlar

        sonuç = QWidget()
        sonuç_layout = QVBoxLayout()
        self.sonuç = QTextEdit()
        self.kaydet = QPushButton("Kaydet")
        self.kaydet.clicked.connect(self.out)



        #Main Window

        tabs.addTab(filtrele, "Filtrele")
        tabs.addTab(ekle, "Ekle/Çıkar")
        general_layout.addWidget(tabs)
        self.setLayout(general_layout)


    #slot
    def filtrele(self):
        self.criterias[0] = self.tc.text().lower()
        self.criterias[1] = self.isim.text().lower()
        self.criterias[2] = self.soyisim.text().lower()
        self.criterias[3] = self.yaş.text().lower()
        self.criterias[4] = self.telno.text().lower()
        self.criterias[5] = self.adres.text().lower()
        self.criterias[6] = str(self.genel_bölge.currentIndex())
        self.criterias[7] = str(self.ihtiyaç_sınıfı.currentIndex())
        self.criterias[8] = str(self.özel_durum.currentIndex())
        self.criterias[9] = str(self.ihtiyaç_seviyesi.currentIndex())
        self.criterias[10] = str(self.yardım.currentIndex())
        temp = self.data.copy()[1:]
        for k in range(11):
            if self.criterias[k] == "" or self.criterias[k] == None or self.criterias[k] == "0":
                continue
            else:
                temp = list(filter(lambda x: self.criterias[k] in x[k], temp))
        self.tc.setText("")
        self.isim.setText("")
        self.yaş.setText("")
        self.telno.setText("")
        self.adres.setText("")
        self.genel_bölge.setCurrentIndex(0)
        self.ihtiyaç_sınıfı.setCurrentIndex(0)
        self.özel_durum.setCurrentIndex(0)
        self.ihtiyaç_seviyesi.setCurrentIndex(0)
        self.yardım.setCurrentIndex(0)
        print(temp)
        self.result = temp

    def filtrele2(self):
        self.criterias[0] = self.tc_ekle.text().lower()
        self.criterias[1] = self.isim_ekle.text().lower()
        self.criterias[2] = self.soyisim_ekle.text().lower()
        self.criterias[3] = self.yaş_ekle.text().lower()
        self.criterias[4] = self.telno_ekle.text().lower()
        self.criterias[5] = self.adres_ekle.text().lower()
        self.criterias[6] = str(self.genel_bölge_ekle.currentIndex())
        self.criterias[7] = str(self.ihtiyaç_sınıfı_ekle.currentIndex())
        self.criterias[8] = str(self.özel_durum_ekle.currentIndex())
        self.criterias[9] = str(self.ihtiyaç_seviyesi_ekle.currentIndex())
        self.criterias[10] = str(self.yardım_ekle.currentIndex())
        temp = self.data.copy()[1:]
        for k in range(11):
            if self.criterias[k] == "" or self.criterias[k] == None or self.criterias[k] == "0":
                continue
            else:
                temp = list(filter(lambda x: self.criterias[k] in x[k], temp))
        self.tc_ekle.setText("")
        self.isim_ekle.setText("")
        self.yaş_ekle.setText("")
        self.telno_ekle.setText("")
        self.adres_ekle.setText("")
        self.genel_bölge_ekle.setCurrentIndex(0)
        self.ihtiyaç_sınıfı_ekle.setCurrentIndex(0)
        self.özel_durum_ekle.setCurrentIndex(0)
        self.ihtiyaç_seviyesi_ekle.setCurrentIndex(0)
        self.yardım_ekle.setCurrentIndex(0)
        print(temp)
        self.result = temp


    def ekle(self):
        check = True
        self.criterias[0] = self.tc_ekle.text().lower()
        self.criterias[1] = self.isim_ekle.text().lower()
        self.criterias[2] = self.soyisim_ekle.text().lower()
        self.criterias[3] = self.yaş_ekle.text().lower()
        self.criterias[4] = self.telno_ekle.text().lower()
        self.criterias[5] = self.adres_ekle.text().lower()
        self.criterias[6] = str(self.genel_bölge_ekle.currentIndex())
        self.criterias[7] = str(self.ihtiyaç_sınıfı_ekle.currentIndex())
        self.criterias[8] = str(self.özel_durum_ekle.currentIndex())
        self.criterias[9] = str(self.ihtiyaç_seviyesi_ekle.currentIndex())
        self.criterias[10] = str(self.yardım_ekle.currentIndex())
        for k in self.criterias:
            if k == "" or k == None:
                res = QMessageBox.information(self, "Eksik bilgi!", "Lütfen tüm alanları doldurduğunuzdan emin olunuz", QMessageBox.StandardButton.Ok)
                check = False
                break
        if check:
            try:
                with open("database.csv", "a") as file:
                    file.write("\n")
                    string = ",".join(self.criterias.copy())
                    file.write(string)
                    self.data.append(self.criterias)
                res = QMessageBox.information(self, "Eklendi", "Kişi listeye eklendi.", QMessageBox.StandardButton.Ok)
            except:
                res = QMessageBox.information(self, "Hata!", "Bir hata oluştu.", QMessageBox.StandardButton.Ok)



    def çıkar(self):
        self.filtrele2()
        print(self.result)
        res = QMessageBox.question(self, "Sil", f"Bulunan {len(self.result)} kişiyi silmek istediğinizden emin misiniz?",
                                   QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if res == QMessageBox.StandardButton.Yes:
            new = self.data.copy()
            for k in self.result:
                index = new.index(k)
                new.pop(index)

            try:
                with open("database.csv", "w") as file:
                    string = ",".join(new[0])
                    file.write(string)
                    for k in range(1, len(new)):
                        string = ",".join(new[k])
                        file.write("\n")
                        file.write(string)

                self.data = new
                res = QMessageBox.information(self, "Silindi", f"{len(self.result)} kişi başarıyla silindi.", QMessageBox.StandardButton.Ok)
            except:
                res = QMessageBox.information(self, "Hata!", "Bir hata oluştu.", QMessageBox.StandardButton.Ok)

    def out(self):
        name = time.ctime().split(" ")
        name = "_".join(name[1:4])
        try:
            with open(f"{str(hash(str(time.time())))}_{name}.txt", "x") as file:
                file.write(self.sonuç.toPlainText())
            res = QMessageBox.information(self, "Kaydedildi!", "Dosya başarıyla kaydedildi.", QMessageBox.StandardButton.Ok)
        except:
            res = QMessageBox.information(self, "Hata!", "Bir hata oluştu.", QMessageBox.StandardButton.Ok)



app = QApplication(sys.argv)

widget = Widget()

widget.show()

app.exec()