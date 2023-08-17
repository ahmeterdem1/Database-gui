import csv, sys, time, openpyxl
from PySide6.QtWidgets import QApplication, QPushButton, QLabel, QWidget, \
    QVBoxLayout, QMessageBox, QTabWidget, QComboBox, QHBoxLayout, QLineEdit, QTextEdit, QCheckBox

class Widget(QWidget):

    def __init__(self):
        super().__init__()
        self.data = 0
        self.criterias = [None] * 13
        self.result = list()
        self.result_asıl = list()
        self.genelBölge = {"1": "Bölge 1", "2": "Bölge 2", "3": "Bölge 3", "4": "Bölge 4", "5": "Bölge 5", "6": "Bölge 6", "7": "Bölge 7",
                           "8": "Bölge 8", "9": "Bölge 9", "10": "Bölge 10", "11": "Bölge 11", "0": ""}
        self.ihtiyaçSınıfı = {"1": "Bir", "2": "İki", "3": "Üç", "4": "Dört", "5": "Beş", "6": "Altı", "7": "Yedi", "0": ""}
        self.özelDurum = {"1": "Bir", "2": "İki", "3": "Üç", "4": "Dört", "5": "Beş", "0": ""}
        self.ihtiyaçSeviyesi = {"1": "En düşük", "2": "Düşük", "3": "Orta", "4": "Yüksek", "5": "En yüksek", "0": ""}
        self.yardımAlma = {"2": "Yardım alıyor", "1": "Yardım almıyor", "0": ""}
        self.çeşit = ["Gıda - Kıyafet", "Barınma", "Eğitim - Burs", "Sağlık", "Yaşlı - Engelli Bakım", "Kriz"]
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
        self.genel_bölge.addItem("Bölge 1")
        self.genel_bölge.addItem("Bölge 2")
        self.genel_bölge.addItem("Bölge 3")
        self.genel_bölge.addItem("Bölge 4")
        self.genel_bölge.addItem("Bölge 5")
        self.genel_bölge.addItem("Bölge 6")
        self.genel_bölge.addItem("Bölge 7")
        self.genel_bölge.addItem("Bölge 8")
        self.genel_bölge.addItem("Bölge 9")
        self.genel_bölge.addItem("Bölge 10")
        self.genel_bölge.addItem("Bölge 11")
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
        self.ihtiyaç_seviyesi.addItem("En düşük")
        self.ihtiyaç_seviyesi.addItem("Düşük")
        self.ihtiyaç_seviyesi.addItem("Orta")
        self.ihtiyaç_seviyesi.addItem("Yüksek")
        self.ihtiyaç_seviyesi.addItem("En yüksek")
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

        aile_widget = QWidget()
        aile = QHBoxLayout()
        aile1 = QLabel("Aile büyüklüğü: ")
        aile2 = QLineEdit()
        self.aile = aile2
        aile.addWidget(aile1)
        aile.addWidget(aile2)
        aile_widget.setLayout(aile)

        yardım_aile = QWidget()
        yardım_aile_layout = QHBoxLayout()
        yardım_aile_layout.addWidget(yardım_widget)
        yardım_aile_layout.addWidget(aile_widget)
        yardım_aile.setLayout(yardım_aile_layout)

        çeşit_widget = QWidget()
        çeşit = QHBoxLayout()
        çeşit1 = QCheckBox("Gıda - Kıyafet")
        çeşit1.toggled.connect(self.kontrol_unchecker)
        çeşit2 = QCheckBox("Barınma")
        çeşit2.toggled.connect(self.kontrol_unchecker)
        çeşit3 = QCheckBox("Eğitim - Burs")
        çeşit3.toggled.connect(self.kontrol_unchecker)
        çeşit4 = QCheckBox("Sağlık")
        çeşit4.toggled.connect(self.kontrol_unchecker)
        çeşit5 = QCheckBox("Yaşlı - Engelli Bakım")
        çeşit5.toggled.connect(self.kontrol_unchecker)
        çeşit6 = QCheckBox("Kriz")
        çeşit6.toggled.connect(self.kontrol_unchecker)
        self.kontrol = QCheckBox("Hiçbiri")
        self.kontrol.setChecked(1)
        self.çeşit_list = [çeşit1, çeşit2, çeşit3, çeşit4, çeşit5, çeşit6]
        çeşit.addWidget(çeşit1)
        çeşit.addWidget(çeşit2)
        çeşit.addWidget(çeşit3)
        çeşit.addWidget(çeşit4)
        çeşit.addWidget(çeşit5)
        çeşit.addWidget(çeşit6)
        çeşit.addWidget(self.kontrol)
        self.kontrol.toggled.connect(self.unchecker)
        çeşit_widget.setLayout(çeşit)

        self.ara = QPushButton("Filtrele")
        self.ara.clicked.connect(self.filtrele)

        filtrele_layout.addWidget(tc_isim)
        filtrele_layout.addWidget(soyisim_yaş)
        filtrele_layout.addWidget(telno_adres)
        filtrele_layout.addWidget(genel_bölge_ihtiyaç_sınıfı)
        filtrele_layout.addWidget(özel_durum_ihtiyaç_seviyesi)
        filtrele_layout.addWidget(yardım_aile)
        filtrele_layout.addWidget(çeşit_widget)
        filtrele_layout.addWidget(self.ara)
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
        self.genel_bölge_ekle.addItem("Bölge 1")
        self.genel_bölge_ekle.addItem("Bölge 2")
        self.genel_bölge_ekle.addItem("Bölge 3")
        self.genel_bölge_ekle.addItem("Bölge 4")
        self.genel_bölge_ekle.addItem("Bölge 5")
        self.genel_bölge_ekle.addItem("Bölge 6")
        self.genel_bölge_ekle.addItem("Bölge 7")
        self.genel_bölge_ekle.addItem("Bölge 8")
        self.genel_bölge_ekle.addItem("Bölge 9")
        self.genel_bölge_ekle.addItem("Bölge 10")
        self.genel_bölge_ekle.addItem("Bölge 11")
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
        self.ihtiyaç_seviyesi_ekle.addItem("En düşük")
        self.ihtiyaç_seviyesi_ekle.addItem("Düşük")
        self.ihtiyaç_seviyesi_ekle.addItem("Orta")
        self.ihtiyaç_seviyesi_ekle.addItem("Yüksek")
        self.ihtiyaç_seviyesi_ekle.addItem("En yüksek")
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

        aile_ekle_widget = QWidget()
        aile_ekle = QHBoxLayout()
        aile1_ekle = QLabel("Aile büyüklüğü: ")
        aile2_ekle = QLineEdit()
        self.aile_ekle = aile2_ekle
        aile_ekle.addWidget(aile1_ekle)
        aile_ekle.addWidget(aile2_ekle)
        aile_ekle_widget.setLayout(aile_ekle)

        yardım_aile_ekle = QWidget()
        yardım_aile_ekle_layout = QHBoxLayout()
        yardım_aile_ekle_layout.addWidget(yardım_ekle_widget)
        yardım_aile_ekle_layout.addWidget(aile_ekle_widget)
        yardım_aile_ekle.setLayout(yardım_aile_ekle_layout)

        çeşit_ekle_widget = QWidget()
        çeşit_ekle = QHBoxLayout()
        çeşit1_ekle = QCheckBox("Gıda - Kıyafet")
        çeşit1_ekle.toggled.connect(self.kontrol_unchecker_ekle)
        çeşit2_ekle = QCheckBox("Barınma")
        çeşit2_ekle.toggled.connect(self.kontrol_unchecker_ekle)
        çeşit3_ekle = QCheckBox("Eğitim - Burs")
        çeşit3_ekle.toggled.connect(self.kontrol_unchecker_ekle)
        çeşit4_ekle = QCheckBox("Sağlık")
        çeşit4_ekle.toggled.connect(self.kontrol_unchecker_ekle)
        çeşit5_ekle = QCheckBox("Yaşlı - Engelli Bakım")
        çeşit5_ekle.toggled.connect(self.kontrol_unchecker_ekle)
        çeşit6_ekle = QCheckBox("Kriz")
        çeşit6_ekle.toggled.connect(self.kontrol_unchecker_ekle)
        self.kontrol_ekle = QCheckBox("Hiçbiri")
        self.kontrol_ekle.setChecked(1)
        self.çeşit_ekle_list = [çeşit1_ekle, çeşit2_ekle, çeşit3_ekle, çeşit4_ekle, çeşit5_ekle, çeşit6_ekle]
        çeşit_ekle.addWidget(çeşit1_ekle)
        çeşit_ekle.addWidget(çeşit2_ekle)
        çeşit_ekle.addWidget(çeşit3_ekle)
        çeşit_ekle.addWidget(çeşit4_ekle)
        çeşit_ekle.addWidget(çeşit5_ekle)
        çeşit_ekle.addWidget(çeşit6_ekle)
        çeşit_ekle.addWidget(self.kontrol_ekle)
        self.kontrol_ekle.toggled.connect(self.unchecker_ekle)
        çeşit_ekle_widget.setLayout(çeşit_ekle)

        self.add = QPushButton("Ekle")
        self.drop = QPushButton("Çıkar")
        self.add.clicked.connect(self.ekle)
        self.drop.clicked.connect(self.çıkar)

        ekle_çıkar = QWidget()
        ekle_çıkar_layout = QHBoxLayout()
        ekle_çıkar_layout.addWidget(self.add)
        ekle_çıkar_layout.addWidget(self.drop)
        ekle_çıkar.setLayout(ekle_çıkar_layout)

        ekle_layout.addWidget(tc_isim_ekle)
        ekle_layout.addWidget(soyisim_yaş_ekle)
        ekle_layout.addWidget(telno_adres_ekle)
        ekle_layout.addWidget(genel_bölge_ihtiyaç_sınıfı_ekle)
        ekle_layout.addWidget(özel_durum_ihtiyaç_seviyesi_ekle)
        ekle_layout.addWidget(yardım_aile_ekle)
        ekle_layout.addWidget(çeşit_ekle_widget)
        ekle_layout.addWidget(ekle_çıkar)
        ekle.setLayout(ekle_layout)

        #sonuçlar

        sonuç = QWidget()
        sonuç_layout = QVBoxLayout()
        self.sonuç = QTextEdit()
        self.kaydet = QPushButton("Kaydet")
        self.kaydet.clicked.connect(self.excel_save)
        sonuç_layout.addWidget(self.sonuç)
        sonuç_layout.addWidget(self.kaydet)
        sonuç.setLayout(sonuç_layout)



        #Main Window

        tabs.addTab(filtrele, "Filtrele")
        tabs.addTab(ekle, "Ekle/Çıkar")
        tabs.addTab(sonuç, "Çıktı")
        general_layout.addWidget(tabs)
        self.setLayout(general_layout)


    #slot

    def replacer(self, liste: list):
        text = ""
        for k in liste:
            k[1] = k[1].upper()
            k[2] = k[2].upper()
            k[6] = self.genelBölge[k[6]]
            k[7] = self.ihtiyaçSınıfı[k[7]]
            k[8] = self.özelDurum[k[8]]
            k[9] = self.ihtiyaçSeviyesi[k[9]]
            k[10] = self.yardımAlma[k[10]]
            s = bin(64 + int(k[12]))
            temp = list()
            for x in range(len(s) - 1, 2, -1):
                if s[x] == "1":
                    temp.append(self.çeşit[x - 3])
            k[12] = " / ".join(temp)
            add = " ".join(k)
            text += (add + "\n")
        return text

    def filtrele(self):
        bit = ""
        self.criterias[0] = self.tc.text().lower()
        self.criterias[1] = self.isim.text().lower()
        self.criterias[2] = self.soyisim.text().lower()
        self.criterias[3] = self.yaş.text()
        self.criterias[4] = self.telno.text().lower()
        self.criterias[5] = self.adres.text().lower()
        self.criterias[6] = str(self.genel_bölge.currentIndex())
        self.criterias[7] = str(self.ihtiyaç_sınıfı.currentIndex())
        self.criterias[8] = str(self.özel_durum.currentIndex())
        self.criterias[9] = str(self.ihtiyaç_seviyesi.currentIndex())
        self.criterias[10] = str(self.yardım.currentIndex())
        self.criterias[11] = self.aile.text()
        for k in self.çeşit_list:
            if k.isChecked():
                bit += "1"
            else:
                bit += "0"
        self.criterias[12] = int(bit, 2)
        temp = list()
        print(self.data)
        for k in range(1, len(self.data)):
            temp.append(self.data[k].copy())
        for k in range(13):
            if self.criterias[k] == "" or self.criterias[k] == None or self.criterias[k] == "0" or self.criterias[k] == "*":
                continue
            elif k == 3 and "-" in self.criterias[3]:
                try:
                    field = self.criterias[3].split("-")
                    field = list(range(int(field[0]), int(field[1]) + 1))
                    temp = list(filter(lambda x: int(x[k]) in field, temp))
                except:
                    res = QMessageBox.information(self, "Hata!", "Yaş girdisinde hata oluştu.", QMessageBox.StandardButton.Ok)
            elif k == 6 and self.criterias[k] == "1":
                temp = list(filter(lambda x: self.criterias[k] == x[k], temp))
            elif k == 11 and "-" in self.criterias[11]:
                try:
                    field = self.criterias[11].split("-")
                    field = list(range(int(field[0]), int(field[1]) + 1))
                    temp = list(filter(lambda x: int(x[k]) in field, temp))
                except:
                    res = QMessageBox.information(self, "Hata!", "Aile girdisinde hata oluştu.", QMessageBox.StandardButton.Ok)
            elif k == 12 and not self.kontrol.isChecked():
                temp = list(filter(lambda x: int(x[k]) - self.criterias[k] == 0, temp))
            elif k == 12 and self.kontrol.isChecked():
                continue
            else:
                temp = list(filter(lambda x: self.criterias[k] in x[k], temp))
        self.tc.setText("")
        self.isim.setText("")
        self.soyisim.setText("")
        self.yaş.setText("")
        self.telno.setText("")
        self.adres.setText("")
        self.genel_bölge.setCurrentIndex(0)
        self.ihtiyaç_sınıfı.setCurrentIndex(0)
        self.özel_durum.setCurrentIndex(0)
        self.ihtiyaç_seviyesi.setCurrentIndex(0)
        self.yardım.setCurrentIndex(0)
        self.aile.setText("")
        for k in self.çeşit_list:
            k.setChecked(0)
        self.kontrol.setChecked(1)
        self.result = temp
        self.result_asıl = temp
        self.sonuç.setText(self.replacer(temp))
        res = QMessageBox.information(self, "Filtrelendi", f"{len(temp)} kişi bulundu.", QMessageBox.StandardButton.Ok)

    def filtrele2(self):
        bit = ""
        self.criterias[0] = self.tc_ekle.text().lower()
        self.criterias[1] = self.isim_ekle.text().lower()
        self.criterias[2] = self.soyisim_ekle.text().lower()
        self.criterias[3] = self.yaş_ekle.text()
        self.criterias[4] = self.telno_ekle.text().lower()
        self.criterias[5] = self.adres_ekle.text().lower()
        self.criterias[6] = str(self.genel_bölge_ekle.currentIndex())
        self.criterias[7] = str(self.ihtiyaç_sınıfı_ekle.currentIndex())
        self.criterias[8] = str(self.özel_durum_ekle.currentIndex())
        self.criterias[9] = str(self.ihtiyaç_seviyesi_ekle.currentIndex())
        self.criterias[10] = str(self.yardım_ekle.currentIndex())
        self.criterias[11] = self.aile_ekle.text()
        for k in self.çeşit_ekle_list:
            if k.isChecked():
                bit += "1"
            else:
                bit += "0"
        self.criterias[12] = int(bit, 2)
        temp = list()
        for k in range(1, len(self.data)):
            temp.append(self.data[k].copy())

        for k in range(13):
            if self.criterias[k] == "" or self.criterias[k] == None or self.criterias[k] == "0":
                continue
            elif k == 3 and "-" in self.criterias[3]:
                try:
                    field = self.criterias[3].split("-")
                    field = list(range(int(field[0]), int(field[1]) + 1))
                    temp = list(filter(lambda x: int(x[k]) in field, temp))
                except:
                    res = QMessageBox.information(self, "Hata!", "Yaş girdisinde hata oluştu.", QMessageBox.StandardButton.Ok)
            elif k == 6 and self.criterias[k] == "1":
                temp = list(filter(lambda x: self.criterias[k] == x[k], temp))
            elif k == 11 and "-" in self.criterias[11]:
                try:
                    field = self.criterias[11].split("-")
                    field = list(range(int(field[0]), int(field[1]) + 1))
                    temp = list(filter(lambda x: int(x[k]) in field, temp))
                except:
                    res = QMessageBox.information(self, "Hata!", "Aile girdisinde hata oluştu.", QMessageBox.StandardButton.Ok)
            elif k == 12 and not self.kontrol_ekle.isChecked():
                temp = list(filter(lambda x: int(x[k]) - self.criterias[k] == 0, temp))
            elif k == 12 and self.kontrol_ekle.isChecked():
                continue
            else:
                temp = list(filter(lambda x: self.criterias[k] in x[k], temp))
        self.tc_ekle.setText("")
        self.isim_ekle.setText("")
        self.soyisim_ekle.setText("")
        self.yaş_ekle.setText("")
        self.telno_ekle.setText("")
        self.adres_ekle.setText("")
        self.genel_bölge_ekle.setCurrentIndex(0)
        self.ihtiyaç_sınıfı_ekle.setCurrentIndex(0)
        self.özel_durum_ekle.setCurrentIndex(0)
        self.ihtiyaç_seviyesi_ekle.setCurrentIndex(0)
        self.yardım_ekle.setCurrentIndex(0)
        self.aile_ekle.setText("")
        for k in self.çeşit_ekle_list:
            k.setChecked(0)
        self.kontrol_ekle.setChecked(0)
        self.result = temp.copy()


    def ekle(self):
        check = True
        bit = ""
        self.criterias[0] = self.tc_ekle.text().lower()
        self.criterias[1] = self.isim_ekle.text().lower()
        self.criterias[2] = self.soyisim_ekle.text().lower()
        self.criterias[3] = self.yaş_ekle.text()
        self.criterias[4] = self.telno_ekle.text().lower()
        self.criterias[5] = self.adres_ekle.text().lower()
        self.criterias[6] = str(self.genel_bölge_ekle.currentIndex())
        self.criterias[7] = str(self.ihtiyaç_sınıfı_ekle.currentIndex())
        self.criterias[8] = str(self.özel_durum_ekle.currentIndex())
        self.criterias[9] = str(self.ihtiyaç_seviyesi_ekle.currentIndex())
        self.criterias[10] = str(self.yardım_ekle.currentIndex())
        self.criterias[11] = self.aile_ekle.text()
        if not self.kontrol_ekle.isChecked():
            for k in self.çeşit_ekle_list:
                if k.isChecked():
                    bit += "1"
                else:
                    bit += "0"
            self.criterias[12] = str(int(bit, 2))
        else:
            self.criterias[12] = "0"

        for k in self.criterias:
            if k == "" or k == None:
                res = QMessageBox.information(self, "Eksik bilgi!", "Lütfen tüm alanları doldurduğunuzdan emin olunuz", QMessageBox.StandardButton.Ok)
                check = False
                break
        if check:
            try:
                with open("database.csv", "a") as file:
                    file.write("\n")
                    string = ",".join(self.criterias)
                    file.write(string)
                    self.data.append(self.criterias.copy())
                res = QMessageBox.information(self, "Eklendi", "Kişi listeye eklendi.", QMessageBox.StandardButton.Ok)
            except:
                res = QMessageBox.information(self, "Hata!", "Bir hata oluştu.", QMessageBox.StandardButton.Ok)



    def çıkar(self):
        self.filtrele2()
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

    def excel_save(self):
        liste = [["T.C. Kimlik No", "İsim", "Soyisim", "Yaş", "Tel No", "Adres", "Genel Bölge",
                  "İhtiyaç Sınıfı", "Özel durum", "İhtiyaç Seviyesi", "Yardım alıyor mu?", "Aile Büyüklüğü", "Yardım Çeşidi"]]
        #proper copying executed
        for k in self.result_asıl:
            liste.append(k.copy())
        name = time.ctime().split(" ")
        name = "_".join(name[1:4])
        try:
            wb = openpyxl.Workbook()
            sheet = wb.active
            for k in range(0, len(liste)):
                # doing temp.copy() in the filtration does not change the fact that
                #every element of temp is a list itself and they are not copied individually
                #so any change on temp.copy() will affect temp itself, or vice versa.
                #beware of this fact in future works
                for l in range(0, len(liste[0])):
                    c = sheet.cell(row=k+1, column=l+1)
                    c.value = liste[k][l]
            wb.save(f"{str(hash(str(time.time())))}_{name}.xlsx")
            res = QMessageBox.information(self, "Kaydedildi!", "Dosya başarıyla kaydedildi.",
                                          QMessageBox.StandardButton.Ok)
        except:
            res = QMessageBox.information(self, "Hata!", "Bir hata oluştu.", QMessageBox.StandardButton.Ok)

    def unchecker(self):
        for k in self.çeşit_list:
            k.setChecked(0)

    def unchecker_ekle(self):
        for k in self.çeşit_ekle_list:
            k.setChecked(0)

    def kontrol_unchecker(self):
        self.kontrol.setChecked(0)

    def kontrol_unchecker_ekle(self):
        self.kontrol_ekle.setChecked(0)





app = QApplication(sys.argv)

widget = Widget()

widget.show()

app.exec()