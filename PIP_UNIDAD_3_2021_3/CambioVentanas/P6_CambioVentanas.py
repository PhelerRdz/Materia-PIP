import sys

from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "P6_MainWindow.ui"  # Nombre del archivo

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.btn_abrirWidget.clicked.connect(self.widget)
        self.btn_abrirDialog.clicked.connect(self.dialog)

    def widget(self):
        self.ventana = MyAppW()
        self.ventana.setWindowModality(2)
        self.ventana.show()

    def dialog(self):
        self.ventana = MyAppD()
        self.ventana.setModal(True)
        self.ventana.show()


###################################################################################
###WIDGET

qtCreatorFileW = "P6_Widget.ui"  # Nombre del archivo

Ui_Widget, QtBaseClass = uic.loadUiType(qtCreatorFileW)

class MyAppW(QtWidgets.QWidget, Ui_Widget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        Ui_Widget.__init__(self)
        self.setupUi(self)

###################################################################################
###DIALOG

qtCreatorFileD = "P6_Dialog.ui"  # Nombre del archivo

Ui_Dialog, QtBaseClass = uic.loadUiType(qtCreatorFileD)

class MyAppD(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        Ui_Dialog.__init__(self)
        self.setupUi(self)

###################################################################################

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


