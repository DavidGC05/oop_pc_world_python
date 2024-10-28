from computadora import Computadora
from monitor import Monitor
from orden import Orden
from raton import Raton
from teclado import Teclado
# Creacion obejto computadora2
teclado1 = Teclado('HP', 'USB')
raton1 = Raton('HP', 'USB')
monitor1 = Monitor('HP',  27)
computadora1 = Computadora('HP', monitor1, teclado1, raton1)

# Creacion obejto computadora2
teclado2 = Teclado('Logi', 'USB')
raton2 = Raton('HP', 'Bluetooth')
monitor2 = Monitor('HP', 32)
computadora2 = Computadora('Dell', monitor2, teclado2, raton2)

computadoras1 = [computadora1, computadora2]
orden1 = Orden(computadoras1)
#print(orden1)

teclado3 = Teclado('Apple', 'Bluetooth')
raton3 = Raton('Apple', 'Bluetooth')
monitor3 = Monitor('Apple', 27)
computadora3 = Computadora('Apple', monitor3, teclado2, raton1)

orden1.agregar_computadora(computadora3)
print(orden1)