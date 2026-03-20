from producto import *

class Cromos(Producto):
    def __init__(self, nombre, marca, edicion, copias, estado):
        super().__init__(nombre, marca, copias, estado)
        self.edicion = edicion
# Calcular precio
    def precio(self):
        if self.copias <= 10:
            return (4 ** self.estado) / max(1, self.copias)
        else:
            return (3 ** self.estado) / max(1, self.copias)

    def __str__(self):
        return f'Cromo: {self.nombre} ({self.edicion}) - Estado: {self.estado}'