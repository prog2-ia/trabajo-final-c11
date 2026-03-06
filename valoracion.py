class Valoracion:
    def __init__(self, centrado, esquinas, bordes, superficies, mueescas, limpieza, piezas_faltantes):
        self.centrado = centrado
        self.esquinas = esquinas
        self.bordes = bordes
        self.superficies = superficies

    def validar_centrado(self, centrado):#Con dato numérico
        if centrado < 0 or centrado > 10:
            return False
        else:
            return True
    def validar_esquinas(self, esquinas):
        if esquinas < 0 or esquinas > 10:
            return False
        else:
            return True
    def validar_bordes(self, bordes):
        if bordes < 0 or bordes > 10:
            return False
        else:
            return True
    def validar_superficies(self, superficies):
        if superficies < 0 or superficies > 10:
            return False
        else:
            return True

    def nota_cromo(self):
        nota_cromo = (self.centrado + self.esquinas + self.bordes + self.superficies) / 4
        return nota_cromo

    def mostrar_cromo(self, nota):
        print('--Valoración del cromo--')
        print('Nota:', {nota})
        print('Centrado:', {self.centrado})
        print('Esquinas:', {self.esquinas})
        print('Bordes:', {self.bordes})
        print('Superficies:', {self.superficies})

    def validar_muescas(self, mueescas):
        if mueescas < 0 or mueescas > 10:
            return False
        else:
            return True
    def validar_limpieza(self, limpieza):
        if limpieza < 0 or limpieza > 10:
            return False
        else:
            return True
    def validar_piezas_faltantes(self, piezas_faltantes):
        if piezas_faltantes < 0 or piezas_faltantes > 10:
            return False
        else:
            return True
    def nota_figura(self, figura):
        nota_figura = (self.limpieza - (self.muescas/2) - (self.piezas_faltantes/2))
        if nota_figura < 0:
            nota_figura = 0
        return nota_figura
