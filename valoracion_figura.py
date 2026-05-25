from valoracion import Valoracion

class ValoracionFigura(Valoracion):
    def __init__(self, limpieza: float, muescas: float, piezas_faltantes: float) -> None:
        self.limpieza: float = limpieza
        self.muescas: float = muescas
        self.piezas_faltantes: float = piezas_faltantes

    def calcular_nota(self) -> float:
        nota: float = self.limpieza - (self.muescas / 2) - (self.piezas_faltantes / 2)
        return max(0.0, nota)