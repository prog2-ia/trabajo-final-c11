from productos import *

class Figura(Productos):
    contador = 0
    def __init__(self, nombre, marca, modelo, copias, alto, ancho, largo, estado):
        super().__init__(nombre, marca, copias, estado)
        self.modelo = modelo
        self.alto = alto
        self.ancho = ancho
        self.largo = largo
        type(self).contador += 1

    def __str__(self):
        return (f'{self.nombre} - {self.marca} ({self.modelo}) '
                f'Rareza: {self.rarezas()} '
                f'Tamaño: {self.tam()} ({self.ancho},{self.alto},{self.largo}) '
                f'Precio: {self.precio()}')

    def tam(self):
        return self.alto * self.largo * self.ancho

    def rarezas(self):
        super().rarezas()

    def precio(self):
        super().precio()

    def restaurar(self, mejora):
        estado_anterior = self.estado
        self.estado = min(10, self.estado + mejora)
        print(f'{self.nombre} restaurada. Estado: {estado_anterior} -> {self.estado}')

    def categoria_tamano(self):
        if self.alto < 10:
            return 'Miniatura'
        elif 10 <= self.alto <= 30:
            return 'Escala estándar (1/12 o 1/6)'
        else:
            return 'Gran formato / Estatua'

    def ficha_tecnica(self):
        print('-' * 30)
        print(f'FICHA TÉCNICA: {self.nombre}')
        print('-' * 30)
        print(f'Marca/Modelo: {self.marca} / {self.modelo}')
        print(f'Dimensiones:  {self.alto}x{self.ancho}x{self.largo} cm (Volumen: {self.tam()} cm³)')
        print(f'Copias/Rareza: {self.copias} ({self.rarezas()})')
        print(f'Estado:       {self.estado}')
        print(f'Valor Est.:   {round(self.precio(), 2)} euros')
        print('-' * 30)