from producto import *

class Figura(Producto):
    def __init__(self, nombre: str, marca: str, modelo: str, copias: int, alto: float, ancho: float, largo: float, estado: int):
        super().__init__(nombre, marca, copias, estado)
        self.modelo: str = modelo
        self.alto: float = alto
        self.ancho: float = ancho
        self.largo: float = largo
# Calcula el volumen de la figura
    def tam(self) -> float:
        return self.alto * self.largo * self.ancho
# Calcula el precio
    def precio(self) -> float:
        return float((3 ** self.estado) / max(1, self.copias)) * self.tam()

    def __str__(self) -> str:
        return f'Figura: {self.nombre} ({self.modelo}) - Estado: {self.estado}'