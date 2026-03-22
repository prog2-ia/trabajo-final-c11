from valoracion import Valoracion

class ValoracionCromo(Valoracion):
    def __init__(self, centrado, esquinas, bordes, superficies):
        self.centrado = centrado
        self.esquinas = esquinas
        self.bordes = bordes
        self.superficies = superficies
# Calcula la nota de los cromos
    def calcular_nota(self):
        return (self.centrado + self.esquinas + self.bordes + self.superficies) / 4