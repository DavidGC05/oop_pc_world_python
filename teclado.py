# Teclado
from dispositivo_entrada import DispositivoEntrada

class Teclado(DispositivoEntrada):
    contador_teclados = 0
    def __init__(self, marca, tipo_entrada):
        Teclado.contador_teclados += 1
        self.id_teclados = Teclado.contador_teclados
        super().__init__(marca, tipo_entrada)
    def __str__(self):
        return (f'Id: {self.id_teclados}, Marca: {self.marca},'
                f'Tipo entrada: {self.tipo_entrada}')
# Codigo Principal
if __name__ == '__main__':
    teclado1 = Teclado('hp', 'USB')
    print(teclado1)
    teclado2 = Teclado('Logi', 'Bluetooth')
    print(teclado2)