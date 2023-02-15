from notifypy import Notify 
import random as r
    
def notificacion(title='Titulo', message='Hola Mundo!', application_name='App1'):
    notification = Notify()
    notification.title = title
    notification.message = message
    notification.application_name = application_name
    notification.send()

class Divisible:
    
    def __init__(self):
        self.divisible_var = 0
        self.div_igualdad = ''
        self.numDecorator = 0
        self.divisibles = {}
        self.div1 = ''
        self.div2 = ''
        self.num = 0


    def decorar(self, num, num1=''):
        for x, z in enumerate(str(num)):
            num1 += z
            
            if len(str(num))-len(num1) == 3: 
                num1 += '.'
        
        return num1

    def azar_num(self, *args): #* Numero al azar

        if self.divisible_var == 0: 
            self.divisible_var = r.randint(2, 11)
        
        self.num = r.choice([x for x in range(100, 100000, 1) if x % self.divisible_var == 0])
        self.numDecorator = self.decorar(self.num)
                
    def divisible(self): #* Divisibilidad del Numero
        if self.num % 1 == 0: 
            self.divisibles.update(  n1= [int(self.num)//1, self.decorar(int(self.num)//1)] )
        
        if self.num % 2 == 0: 
            self.divisibles.update(  n2= [int(self.num)//2,  self.decorar(int(self.num)//2) ] )
        
        if self.num % 3 == 0: 
            self.divisibles.update(  n3= [int(self.num)//3,  self.decorar(int(self.num)//3) ] )
        
        if self.num % 4 == 0: 
            self.divisibles.update(  n4= [int(self.num)//4,  self.decorar(int(self.num)//4) ] )
        
        if self.num % 5 == 0: 
            self.divisibles.update(  n5= [int(self.num)//5,  self.decorar(int(self.num)//5) ] )
        
        if self.num % 6 == 0: 
            self.divisibles.update(  n6= [int(self.num)//6,  self.decorar(int(self.num)//6) ] )
        
        if self.num % 7 == 0: 
            self.divisibles.update(  n7= [int(self.num)//7,  self.decorar(int(self.num)//7) ] )
        
        if self.num % 8 == 0: 
            self.divisibles.update(  n8= [int(self.num)//8,  self.decorar(int(self.num)//8) ] )
        
        if self.num % 9 == 0: 
            self.divisibles.update(  n9= [int(self.num)//9,  self.decorar(int(self.num)//9) ] )
        
        if self.num % 10 == 0: 
            self.divisibles.update(n10= [int(self.num)//10, self.decorar(int(self.num)//10)] )
        
        if self.num % 11 == 0: 
            self.divisibles.update(n11= [int(self.num)//11, self.decorar(int(self.num)//11)] )

    def encontrar_igualdad(self, div1, div2):
        n = []

        for x in div1: 
            for z in div2: 
                if x == z: n += [x]

        return n

    def fraccion_divisible(self):
        n = Divisible()
        n.azar_num()
        n.divisible()
        
        self.divisible_var = n.divisible_var
        self.azar_num()
        self.divisible()

        self.div1 = n.divisibles
        self.div2 = self.divisibles
        self.div_igualdad = self.encontrar_igualdad(n.divisibles, self.divisibles)

        # return [
        #     n.divisibles, self.divisibles, )
        # ]


    def ordenar_str(self, txt='Hola Mundo!', numLong=20):
        list_txt = txt.split()
        text_return = '' 
        text2 = ''
        i = 0

        for text1 in list_txt:

            if len(f'{text2} {text1}') <= numLong:
                if i != 0: text2 += f' {text1}'
                else: text2 += f'{text1}'

            else:
                text_return += f'{text2}\n'
                text2 = text1
                # if list_txt[-1] == text1: text_return += f'{text2}\n'
            
            i += 1

        return text_return + text2
    
    def set_copia(self, txt='', lista=[]):
        if txt not in lista: lista.append(txt)
        return lista


def main():
    d = Divisible()
    print(d.fraccion_divisible())

if __name__ == '__main__':
    main()

#* Author: Francisco Velez
