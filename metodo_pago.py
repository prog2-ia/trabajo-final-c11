from abc import ABC, abstractmethod

class MetodoPago(ABC):#
    def __init__(self, titular):
        self.titular = titular
    @abstractmethod
    def procesar_pago(self, cantidad):
        pass

    def __str__(self):
        return f'Metodo de pago de {self.titular}'