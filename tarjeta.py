from metodo_pago import MetodoPago

class Tarjeta(MetodoPago):#
    def __init__(self, titular, numero_tarjeta):
        super().__init__(titular)
        self.__numero_tarjeta = numero_tarjeta

    def procesar_pago(self, cantidad):
        print(f'Cobrando {round(cantidad,2)}€ a la tarjeta terminada en {self.numero_tarjeta[-4:]}...')
        return True