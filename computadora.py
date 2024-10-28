from monitor import Monitor
from raton import Raton
from teclado import Teclado


class Computadora:
    contador_computadora = 0
    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_computadora += 1
        self.id_computadora = Computadora.contador_computadora
        self.nombre = nombre
        self.monitor = monitor
        self.teclado = teclado
        self.raton = raton

    def __str__(self):
        return f'''{self.nombre}: {self.id_computadora}
        Monitor: {self.monitor}
        Teclado: {self.teclado}
        Raton: {self.raton}'''
# Codigo principal
if __name__ == '__main__':
    teclado1 = Teclado('HP', 'USB')
    raton1 = Raton('HP', 'USB')
    monitor1 = Monitor('HP',  27)
    computadora1 = Computadora('HP', monitor1, teclado1, raton1)
    print(computadora1)
    teclado2 = Teclado('Logi', 'USB')
    raton2 = Raton('HP', 'Bluetooth')
    monitor2 = Monitor('HP', 32)
    computadora2 = Computadora('Dell', monitor2, teclado2, raton2)
    print(computadora2)
