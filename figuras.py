from producto import *

class Figura(Producto):
    def __init__(self, nombre, marca, modelo, copias, alto, ancho, largo, estado):
        super().__init__(nombre, marca, copias, estado)
        self.modelo = modelo
        self.alto = alto
        self.ancho = ancho
        self.largo = largo

    def tam(self):
        return self.alto * self.largo * self.ancho

    def precio(self):
        return ((3 ** self.estado) / max(1, self.copias)) * self.tam()

    def __str__(self):
        return f'Figura: {self.nombre} ({self.modelo}) - Estado: {self.estado}'