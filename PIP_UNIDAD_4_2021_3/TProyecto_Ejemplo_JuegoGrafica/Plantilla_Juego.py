# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Plantilla_Juego.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FiguraCanvas

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1056, 770)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 200, 601, 511))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_action = QtWidgets.QPushButton(self.centralwidget)
        self.btn_action.setGeometry(QtCore.QRect(770, 490, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_action.setFont(font)
        self.btn_action.setObjectName("btn_action")
        self.btn_arriba = QtWidgets.QPushButton(self.centralwidget)
        self.btn_arriba.setGeometry(QtCore.QRect(770, 570, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_arriba.setFont(font)
        self.btn_arriba.setObjectName("btn_arriba")
        self.btn_izquierda = QtWidgets.QPushButton(self.centralwidget)
        self.btn_izquierda.setGeometry(QtCore.QRect(630, 620, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_izquierda.setFont(font)
        self.btn_izquierda.setObjectName("btn_izquierda")
        self.btn_abajo = QtWidgets.QPushButton(self.centralwidget)
        self.btn_abajo.setGeometry(QtCore.QRect(770, 670, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_abajo.setFont(font)
        self.btn_abajo.setObjectName("btn_abajo")
        self.btn_derecha = QtWidgets.QPushButton(self.centralwidget)
        self.btn_derecha.setGeometry(QtCore.QRect(910, 620, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_derecha.setFont(font)
        self.btn_derecha.setObjectName("btn_derecha")
        self.minutos = QtWidgets.QLabel(self.centralwidget)
        self.minutos.setGeometry(QtCore.QRect(710, 140, 121, 111))
        font = QtGui.QFont()
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.minutos.setFont(font)
        self.minutos.setAlignment(QtCore.Qt.AlignCenter)
        self.minutos.setObjectName("minutos")
        self.txt_tempo_5 = QtWidgets.QLabel(self.centralwidget)
        self.txt_tempo_5.setGeometry(QtCore.QRect(830, 130, 21, 111))
        font = QtGui.QFont()
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.txt_tempo_5.setFont(font)
        self.txt_tempo_5.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_tempo_5.setObjectName("txt_tempo_5")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(410, 150, 211, 41))
        self.label_8.setObjectName("label_8")
        self.segundos = QtWidgets.QLabel(self.centralwidget)
        self.segundos.setGeometry(QtCore.QRect(850, 140, 121, 111))
        font = QtGui.QFont()
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.segundos.setFont(font)
        self.segundos.setAlignment(QtCore.Qt.AlignCenter)
        self.segundos.setObjectName("segundos")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(760, 270, 151, 201))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.rb_normal = QtWidgets.QRadioButton(self.groupBox_2)
        self.rb_normal.setGeometry(QtCore.QRect(30, 100, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.rb_normal.setFont(font)
        self.rb_normal.setObjectName("rb_normal")
        self.tb_facil = QtWidgets.QRadioButton(self.groupBox_2)
        self.tb_facil.setGeometry(QtCore.QRect(30, 150, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.tb_facil.setFont(font)
        self.tb_facil.setObjectName("tb_facil")
        self.rb_dificil = QtWidgets.QRadioButton(self.groupBox_2)
        self.rb_dificil.setGeometry(QtCore.QRect(30, 50, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.rb_dificil.setFont(font)
        self.rb_dificil.setObjectName("rb_dificil")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(120, 0, 801, 91))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap(":/UAT_FIANS/Imagenes/FIANS.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(0, 0, 111, 121))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap(":/NUMEROS/Imagenes/Boca_Juniors_logo18.svg.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(930, 0, 121, 131))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap(":/LOGO/Imagenes/HD-wallpaper-bob-esponja-mafioso-bob-esponja-gangster-mafioso-meme.jpg"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1056, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.figure = plt.figure(figsize=(15, 5))
        self.canvas = FiguraCanvas(self.figure)

        self.ax = self.figure.add_subplot(111)
        # para referir al mismo axes

        self.verticalLayout.addWidget(self.canvas)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_action.setText(_translate("MainWindow", "INICIAR"))
        self.btn_arriba.setText(_translate("MainWindow", "ARRIBA"))
        self.btn_izquierda.setText(_translate("MainWindow", "IZQUIERDA"))
        self.btn_abajo.setText(_translate("MainWindow", "ABAJO"))
        self.btn_derecha.setText(_translate("MainWindow", "DERECHA"))
        self.minutos.setText(_translate("MainWindow", "0"))
        self.txt_tempo_5.setText(_translate("MainWindow", ":"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:18pt; font-weight:600;\">Tiempo Restante:</span></p></body></html>"))
        self.segundos.setText(_translate("MainWindow", "0"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Dificultad"))
        self.rb_normal.setText(_translate("MainWindow", "Normal"))
        self.tb_facil.setText(_translate("MainWindow", "Facil"))
        self.rb_dificil.setText(_translate("MainWindow", "Dificil"))
from TProyecto_Ejemplo_JuegoGrafica import recursos_proyecto_rc
