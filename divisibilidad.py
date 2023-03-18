from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):

    def __style__(self): 
        with open('./style.qss') as f: txt = f.read()
        return txt

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(564, 362)
        
        Form.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        Form.setStyleSheet(self.__style__())

        self.fr_fondo = QtWidgets.QFrame(Form)
        self.fr_fondo.setGeometry(QtCore.QRect(20, 10, 521, 331))
        self.fr_fondo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_fondo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_fondo.setObjectName("fr_fondo")

        self.txte_den = QtWidgets.QLineEdit(self.fr_fondo)
        self.txte_den.setGeometry(QtCore.QRect(300, 160, 101, 51))
        self.txte_den.setMaxLength(6)
        self.txte_den.setAlignment(QtCore.Qt.AlignCenter)
        self.txte_den.setObjectName("txte_den")
        
        self.cb_opc = QtWidgets.QComboBox(self.fr_fondo)
        self.cb_opc.setGeometry(QtCore.QRect(330, 20, 91, 31))
        self.cb_opc.setObjectName("cb_opc")
        self.cb_opc.addItem("")
        self.cb_opc.addItem("")
        self.cb_opc.addItem("")
        self.cb_opc.addItem("")
        self.cb_opc.addItem("")
        self.cb_opc.addItem("")
        self.cb_opc.addItem("")
        self.cb_opc.addItem("")
        self.cb_opc.addItem("")
        self.cb_opc.addItem("")
        self.cb_opc.addItem("")

        self.btn_minimizar = QtWidgets.QPushButton(self.fr_fondo)
        self.btn_minimizar.setGeometry(QtCore.QRect(20, 20, 21, 23))
        self.btn_minimizar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_minimizar.setText("")
        self.btn_minimizar.setObjectName("btn_minimizar")
        
        self.btn_cerrar = QtWidgets.QPushButton(self.fr_fondo)
        self.btn_cerrar.setGeometry(QtCore.QRect(480, 20, 21, 23))
        self.btn_cerrar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_cerrar.setText("")
        self.btn_cerrar.setObjectName("btn_cerrar")
        
        self.lbl_autor = QtWidgets.QLabel(self.fr_fondo)
        self.lbl_autor.setGeometry(QtCore.QRect(0, 280, 221, 51))
        self.lbl_autor.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_autor.setObjectName("lbl_autor")
        
        self.txte_num = QtWidgets.QLineEdit(self.fr_fondo)
        self.txte_num.setGeometry(QtCore.QRect(300, 100, 101, 51))
        self.txte_num.setMaxLength(6)
        self.txte_num.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.txte_num.setAlignment(QtCore.Qt.AlignCenter)
        self.txte_num.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.txte_num.setObjectName("txte_num")

        self.lbl_title = QtWidgets.QLabel(self.fr_fondo)
        self.lbl_title.setGeometry(QtCore.QRect(80, 0, 231, 51))
        self.lbl_title.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_title.setObjectName("lbl_title")
        
        self.btn_verificar = QtWidgets.QPushButton(self.fr_fondo)
        self.btn_verificar.setGeometry(QtCore.QRect(300, 240, 101, 31))
        self.btn_verificar.setObjectName("btn_verificar")
        self.btn_verificar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        
        self.txte_num2 = QtWidgets.QLineEdit(self.fr_fondo)
        self.txte_num2.setEnabled(False)
        self.txte_num2.setGeometry(QtCore.QRect(130, 100, 101, 51))
        self.txte_num2.setAcceptDrops(False)
        self.txte_num2.setMaxLength(6)
        self.txte_num2.setAlignment(QtCore.Qt.AlignCenter)
        self.txte_num2.setPlaceholderText("")
        self.txte_num2.setClearButtonEnabled(False)
        self.txte_num2.setObjectName("txte_num2")
        
        self.txte_den2 = QtWidgets.QLineEdit(self.fr_fondo)
        self.txte_den2.setEnabled(False)
        self.txte_den2.setGeometry(QtCore.QRect(130, 160, 101, 51))
        self.txte_den2.setMaxLength(6)
        self.txte_den2.setAlignment(QtCore.Qt.AlignCenter)
        self.txte_den2.setObjectName("txte_den2")

        self.lbl_igual = QtWidgets.QLabel(self.fr_fondo)
        self.lbl_igual.setGeometry(QtCore.QRect(240, 140, 47, 41))
        self.lbl_igual.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_igual.setObjectName("lbl_igual")

        self.retranslateUi(Form)

        self.btn_minimizar.clicked.connect(Form.showMinimized) 
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Divisibilidad Fracciones"))

        self.cb_opc.setItemText(0, _translate("Form", "2da"))
        self.cb_opc.setItemText(1, _translate("Form", "3ra"))
        self.cb_opc.setItemText(2, _translate("Form", "4ta"))
        self.cb_opc.setItemText(3, _translate("Form", "5ta"))
        self.cb_opc.setItemText(4, _translate("Form", "6ta"))
        self.cb_opc.setItemText(5, _translate("Form", "7ma"))
        self.cb_opc.setItemText(6, _translate("Form", "8va"))
        self.cb_opc.setItemText(7, _translate("Form", "9na"))
        self.cb_opc.setItemText(8, _translate("Form", "10ma"))
        self.cb_opc.setItemText(9, _translate("Form", "11va"))

        self.lbl_autor.setText(_translate("Form", "Autor: Francisco Velez"))
        self.lbl_title.setText(_translate("Form", "Tiene:"))

        self.btn_verificar.setText(_translate("Form", "Verificar"))
        
        self.txte_num2.setText(_translate("Form", "1234"))
        self.txte_den2.setText(_translate("Form", "123456"))
        
        self.lbl_igual.setText(_translate("Form", "="))

#* Author: Francisco Velez
