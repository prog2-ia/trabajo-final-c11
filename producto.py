from abc import ABC, abstractmethod

class Producto(ABC):
    def __init__(self, nombre, marca, copias, estado):
        self.nombre = nombre
        self.marca = marca
        self.copias = copias
        self.estado = estado

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, valor):
        if 0 <= valor <= 10:
            self.__estado = valor
        else:
            print('Error: El estado debe estar entre 0 y 10. Se asignará 0.')
            self.__estado = 0

    @abstractmethod
    def precio(self):
        pass

    def rarezas(self):
        rareza = ''
        if self.copias > 1000000:
            rareza = 'común'
        elif self.copias <= 10:
            rareza = 'único'
        else:
            rareza = 'estándar'
        return rareza