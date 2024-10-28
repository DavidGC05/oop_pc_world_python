# Monitor
class Monitor:
    contador_monitores = 0
    def __init__(self, marca, tamanio):
        Monitor.contador_monitores += 1
        self.id_monitores = Monitor.contador_monitores
        self.marca = marca
        self.tamanio = tamanio

    def __str__(self):
        return (f'Id: {self.id_monitores}, Marca: {self.marca},'
                f'Tamanio: {self.tamanio}')
# Codigo principal
if __name__ == '__main__':
    monitor1 = Monitor('Hp', '15')
    print(monitor1)