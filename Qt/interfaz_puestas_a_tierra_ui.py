# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaz_puestas_a_tierra.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QStackedWidget, QStatusBar, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(854, 643)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(16, 10, 181, 26))
        self.label.setAlignment(Qt.AlignCenter)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(40, 50, 891, 541))
        self.page_0 = QWidget()
        self.page_0.setObjectName(u"page_0")
        self.tableWidget = QTableWidget(self.page_0)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(20, 190, 256, 331))
        self.groupBox_2 = QGroupBox(self.page_0)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(20, 20, 371, 120))
        self.label_16 = QLabel(self.groupBox_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(11, 27, 141, 16))
        self.path_lb = QLabel(self.groupBox_2)
        self.path_lb.setObjectName(u"path_lb")
        self.path_lb.setGeometry(QRect(10, 70, 341, 21))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.path_lb.setFont(font)
        self.path_lb.setStyleSheet(u"color:rgba(0, 0, 0, 140);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";")
        self.pushButton_e = QPushButton(self.groupBox_2)
        self.pushButton_e.setObjectName(u"pushButton_e")
        self.pushButton_e.setGeometry(QRect(280, 20, 75, 24))
        self.pushButton_g = QPushButton(self.page_0)
        self.pushButton_g.setObjectName(u"pushButton_g")
        self.pushButton_g.setGeometry(QRect(290, 140, 75, 24))
        self.pushButton_c = QPushButton(self.page_0)
        self.pushButton_c.setObjectName(u"pushButton_c")
        self.pushButton_c.setGeometry(QRect(30, 140, 75, 24))
        self.groupBox = QGroupBox(self.page_0)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(410, 30, 211, 151))
        self.line_rho_01 = QLineEdit(self.groupBox)
        self.line_rho_01.setObjectName(u"line_rho_01")
        self.line_rho_01.setGeometry(QRect(60, 20, 133, 22))
        self.line_rho_02 = QLineEdit(self.groupBox)
        self.line_rho_02.setObjectName(u"line_rho_02")
        self.line_rho_02.setGeometry(QRect(60, 50, 133, 22))
        self.line_h_0 = QLineEdit(self.groupBox)
        self.line_h_0.setObjectName(u"line_h_0")
        self.line_h_0.setGeometry(QRect(60, 80, 133, 22))
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(11, 83, 101, 16))
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(11, 55, 84, 16))
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(11, 27, 141, 16))
        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 110, 41, 16))
        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(60, 110, 131, 22))
        self.groupBox_3 = QGroupBox(self.page_0)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(630, 30, 171, 131))
        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 90, 31, 16))
        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 60, 41, 20))
        self.label_17 = QLabel(self.groupBox_3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(20, 30, 41, 20))
        self.label_rho_1 = QLabel(self.groupBox_3)
        self.label_rho_1.setObjectName(u"label_rho_1")
        self.label_rho_1.setGeometry(QRect(70, 30, 71, 21))
        self.label_rho_1.setFont(font)
        self.label_rho_1.setStyleSheet(u"color:rgba(0, 0, 0, 140);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";")
        self.label_rho_2 = QLabel(self.groupBox_3)
        self.label_rho_2.setObjectName(u"label_rho_2")
        self.label_rho_2.setGeometry(QRect(70, 60, 71, 21))
        self.label_rho_2.setFont(font)
        self.label_rho_2.setStyleSheet(u"color:rgba(0, 0, 0, 140);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";")
        self.label_h = QLabel(self.groupBox_3)
        self.label_h.setObjectName(u"label_h")
        self.label_h.setGeometry(QRect(70, 90, 71, 21))
        self.label_h.setFont(font)
        self.label_h.setStyleSheet(u"color:rgba(0, 0, 0, 140);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";")
        self.groupBox_4 = QGroupBox(self.page_0)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(390, 210, 321, 151))
        self.label_18 = QLabel(self.groupBox_4)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(20, 90, 121, 16))
        self.label_19 = QLabel(self.groupBox_4)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(20, 62, 161, 16))
        self.label_20 = QLabel(self.groupBox_4)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(20, 34, 141, 16))
        self.label_nit = QLabel(self.groupBox_4)
        self.label_nit.setObjectName(u"label_nit")
        self.label_nit.setGeometry(QRect(200, 30, 71, 21))
        self.label_nit.setFont(font)
        self.label_nit.setStyleSheet(u"color:rgba(0, 0, 0, 140);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";")
        self.label_fev = QLabel(self.groupBox_4)
        self.label_fev.setObjectName(u"label_fev")
        self.label_fev.setGeometry(QRect(200, 60, 71, 21))
        self.label_fev.setFont(font)
        self.label_fev.setStyleSheet(u"color:rgba(0, 0, 0, 140);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";")
        self.label_grad = QLabel(self.groupBox_4)
        self.label_grad.setObjectName(u"label_grad")
        self.label_grad.setGeometry(QRect(200, 90, 71, 21))
        self.label_grad.setFont(font)
        self.label_grad.setStyleSheet(u"color:rgba(0, 0, 0, 140);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";")
        self.label_21 = QLabel(self.groupBox_4)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(20, 120, 121, 16))
        self.label_fun = QLabel(self.groupBox_4)
        self.label_fun.setObjectName(u"label_fun")
        self.label_fun.setGeometry(QRect(200, 120, 71, 21))
        self.label_fun.setFont(font)
        self.label_fun.setStyleSheet(u"color:rgba(0, 0, 0, 140);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";")
        self.stackedWidget.addWidget(self.page_0)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.widget_it = QWidget(self.page_1)
        self.widget_it.setObjectName(u"widget_it")
        self.widget_it.setGeometry(QRect(-30, 60, 441, 431))
        self.widget_res = QWidget(self.page_1)
        self.widget_res.setObjectName(u"widget_res")
        self.widget_res.setGeometry(QRect(420, 120, 381, 371))
        self.pushButton_c_2 = QPushButton(self.page_1)
        self.pushButton_c_2.setObjectName(u"pushButton_c_2")
        self.pushButton_c_2.setGeometry(QRect(20, 490, 75, 24))
        self.label_7 = QLabel(self.page_1)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(430, 15, 351, 91))
        self.label_7.setStyleSheet(u"font: 16pt \"Segoe UI\";")
        self.label_9 = QLabel(self.page_1)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 20, 351, 31))
        self.label_9.setStyleSheet(u"font: 16pt \"Segoe UI\";")
        self.stackedWidget.addWidget(self.page_1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">MODELO BICAPA</span></p></body></html>", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Datos", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.path_lb.setText(QCoreApplication.translate("MainWindow", u"Path", None))
        self.pushButton_e.setText(QCoreApplication.translate("MainWindow", u"Explorar", None))
        self.pushButton_g.setText(QCoreApplication.translate("MainWindow", u"Graficar", None))
        self.pushButton_c.setText(QCoreApplication.translate("MainWindow", u"Calcular", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Valores iniciales sugeridos", None))
        self.line_rho_01.setText(QCoreApplication.translate("MainWindow", u"800", None))
        self.line_rho_02.setText(QCoreApplication.translate("MainWindow", u"200", None))
        self.line_h_0.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"h", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"rho_2", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u" rho_1", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"M\u00e9todo", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Resultado del modelo", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"h", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"rho_2", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u" rho_1", None))
        self.label_rho_1.setText("")
        self.label_rho_2.setText("")
        self.label_h.setText("")
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Iteraciones y error", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Gradiente del error", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"N\u00famero de evaluaciones FO", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"N\u00famero de iteraciones", None))
        self.label_nit.setText("")
        self.label_fev.setText("")
        self.label_grad.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Error", None))
        self.label_fun.setText("")
        self.pushButton_c_2.setText(QCoreApplication.translate("MainWindow", u"Calcular", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Comparaci\u00f3n entre los datos de\n"
"Resistividad Aparentes \n"
"Calculados vs Medidos", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Convergencia de par\u00e1metros", None))
    # retranslateUi

