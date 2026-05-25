from producto import *

class Cromos(Producto):
    def __init__(self, nombre: str, marca: str, edicion: str, copias: int, estado: int):
        super().__init__(nombre, marca, copias, estado)
        self.edicion = edicion
# Calcular precio
    def precio(self) -> float:
        if self.copias <= 10:
            return (4 ** self.estado) / max(1, self.copias)
        else:
            return (3 ** self.estado) / max(1, self.copias)

    def __str__(self) -> str:
        return f'Cromo: {self.nombre} ({self.edicion}) - Estado: {self.estado}'