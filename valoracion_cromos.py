from valoracion import Valoracion

class ValoracionCromo(Valoracion):
    def __init__(self, centrado: float, esquinas: float, bordes: float, superficies: float) -> None:
        self.centrado: float = centrado
        self.esquinas: float = esquinas
        self.bordes: float = bordes
        self.superficies: float = superficies

    def calcular_nota(self) -> float:
        return (self.centrado + self.esquinas + self.bordes + self.superficies) / 4