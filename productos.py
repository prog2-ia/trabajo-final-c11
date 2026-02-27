class Productos:
    def __init__(self, nombre, marca, copias, estado):
        self.nombre = nombre
        self.marca = marca
        self.copias = copias
        self.estado = estado

    def rarezas(self):
        rareza = ''
        if self.copias > 1000000:
            rareza = 'común'
        elif self.copias > 100000:
            rareza = 'poco común'
        elif self.copias > 10000:
            rareza = 'raro'
        elif self.copias > 1000:
            rareza = 'super raro'
        elif self.copias > 10:
            rareza = 'ultra raro'
        elif self.copias <= 10:
            rareza = 'único'
        return rareza

    def precio(self):
        precio = (3 ** self.estado / self.copias) * self.tam()
        return precio