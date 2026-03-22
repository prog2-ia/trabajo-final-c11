from abc import ABC, abstractmethod

class Valoracion(ABC):
# Crea el metodo abstracto calcular_nota
    @abstractmethod
    def calcular_nota(self):
        pass
