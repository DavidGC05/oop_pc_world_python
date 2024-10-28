# Subclase Raton
from dispositivo_entrada import DispositivoEntrada

class Raton(DispositivoEntrada):
    contador_ratones = 0

    def __init__(self, marca, tipo_entrada):
        # Le asignamos un valor con variable contador_raton
        Raton.contador_ratones += 1
        # Creamos atributo de id
        self.id_raton = Raton.contador_ratones
        # Mandamos a llamar metodo __init__ de DispositivoEntrada con super()
        # Evitando llamar el metodo que usa super.
        super().__init__(marca, tipo_entrada)
    def __str__(self):
        return  (f'Id: {self.id_raton}, Marca: {self.marca},'
                 f'Tipo de entrada: {self.tipo_entrada}')
