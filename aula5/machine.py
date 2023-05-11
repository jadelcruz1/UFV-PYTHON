# classes

class Machine:
    """ modelagem de uma maquina virtual """

    def __init__(self, start, stop) :
        """ inicializa os atributos de start e stop """
        self.start = start
        self.stop = stop

    def ligar (self):
        """ simula o funcionamento da máquina"""

        print(f"{self.start} está funcionando.")

    def desligar (self):
         """ simula o funcionamento da máquina"""
         print(f"{self.stop} está desligada.")



class Somar:
    """ criando outra classe para teste"""

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def somatorio(self):
        print( self.num1 + self.num2 ) 