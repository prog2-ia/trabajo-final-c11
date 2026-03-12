from valoracion import Valoracion

class ValoracionFigura(Valoracion):
    def __init__(self, limpieza, muescas, piezas_faltantes):
        self.limpieza = limpieza
        self.muescas = muescas
        self.piezas_faltantes = piezas_faltantes

    def calcular_nota(self):
        nota = self.limpieza - (self.muescas / 2) - (self.piezas_faltantes / 2)
        return max(0, nota)