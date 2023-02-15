from divisibilidad import Ui_Form, QtWidgets, QtCore
from funciones import Divisible, notificacion
from subVentana import subVent
import sys

class MainApp(QtWidgets.QMainWindow): 

    def __init__(self, parent=None, *args): 
        super(MainApp, self).__init__(parent=parent) 

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        self.cont = 0
        self.opcs = []
        self.d = Divisible()
        self.d.fraccion_divisible()
        self.num_main = len(self.d.div_igualdad)-1


        self.message = {
            'Error:Campos': 'Error: Los 2 campos no pueden estar vacios.',
            'Error:Num': 'Error: Numero incorrecto:',
            'Correct': 'Correcto.'
        }

        #? Mover ventana
        self.ui.fr_fondo.mouseMoveEvent = self.mover_ventana
        
        self.ui.txte_num2.setText(self.d.div1['n1'][1])
        self.ui.txte_den2.setText(self.d.div2['n1'][1])
        
        print('\n Info1: ' + str(self.d.div1))
        print('\n Info2: ' + str(self.d.div2))

        self.ui.lbl_title.setText(f'{self.num_main} - Simplificar: ')

        self.ui.btn_cerrar.clicked.connect(self.cerrar) 
        self.ui.btn_verificar.clicked.connect(self.verificar)

    def cerrar(self):
        try: self.Form2.close()
        except: pass 
        finally: self.close()

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def mover_ventana(self, event):
        try:
            if self.isMaximized() == False: 
                if event.buttons() == QtCore.Qt.LeftButton:
                    self.move(self.pos() + event.globalPos() - self.clickPosition)
                    self.clickPosition = event.globalPos()
                    event.accept()
        except: pass


    def ventana2(self, text='Hola Mundo!', function_=False):
        geo = self.geometry()
        self.Form2 = QtWidgets.QMainWindow()

        self.ui2 = subVent()
        self.ui2.setupUi(
            self.Form2, [geo.x(), geo.y(), geo.width(),  geo.height()], 
            self.d.ordenar_str(text)
        )

        if function_ != False:
            self.ui2.btn_continuar.clicked.connect(function_)
        else:
            self.ui2.btn_continuar.clicked.connect(self.Form2.close)
        
        self.Form2.show()


    def verificar(self, *args):
        den = self.ui.txte_den.text()
        num = self.ui.txte_num.text()
        verify = {
            '1ra': 'n1',
            '2da': 'n2',
            '3ra': 'n3',
            '4ta': 'n4',
            '5ta': 'n5',
            '6ta': 'n6',
            '7ma': 'n7',
            '8va': 'n8',
            '9na': 'n9',
            '10ma': 'n10',
            '11va': 'n11'
        }
        verif = False
        txt = verify.get(self.ui.cb_opc.currentText(), ' [-] KeyError...')

        try:
            if str(self.d.div1[txt][0]) == num or self.d.div1[txt][1] == num: verif = True
            
            else: 
                if bool(num) == False: self.ventana2(self.message.get('Error:Campos'))
                else: self.ventana2(f'{self.message.get("Error:Num")} {num}')

        except: pass

        finally:
            try:
                if str(self.d.div2[txt][0]) == den or self.d.div2[txt][1] == den: pass 
                else: 
                    if bool(den) == False: self.ventana2(self.message.get('Error:Campos'))
                    else: self.ventana2(f'{self.message.get("Error:Num")} {den}')
                    verif = False

            except: verif = False
        
        if verif: 
            n1 = len(self.opcs)
            self.opcs = self.d.set_copia(self.ui.cb_opc.currentText(), self.opcs)
            n2 = len(self.opcs)
            
            if n1 == n2:
                self.ventana2(
                    text=f'Ya has comprobado: {self.opcs[-1]} falta mas...', function_=self.continuar
                )
            
            else:
                self.num_main -= 1
                self.ventana2(text=self.message.get('Correct'), function_=self.continuar)

    def continuar(self):
        if self.num_main >= 1:
            self.ui.lbl_title.setText(f'{self.num_main} - Tiene: ')
            self.ui.txte_num.setText('')
            self.ui.txte_den.setText('')
            self.Form2.close()

        else:
            self.cont += 1
            
            if self.cont%1 == 0: 
                notificacion(
                    title='Felicitaciones!!!',
                    message=f'Has simplificado {self.cont} fracciones.',
                    application_name=self.windowTitle()
                )

            self.d.fraccion_divisible()
            self.num_main = len(self.d.div_igualdad)-1
            
            self.ui.txte_num2.setText(self.d.div1['n1'][1])
            self.ui.txte_den2.setText(self.d.div2['n1'][1])
            
            self.ui.txte_num.setText('')
            self.ui.txte_den.setText('')

            self.ui.lbl_title.setText(f'{self.num_main} - Tiene: ')
            self.Form2.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv) 
    window = MainApp() 
    window.show() 
    sys.exit(app.exec_())

#* Author: Francisco Velez
