from metodo_pago import MetodoPago

class Transferencia(MetodoPago):#
    def __init__(self, titular, iban):
        super().__init__(titular)
        self.__iban = iban

    def procesar_pago(self, cantidad):
        print(f'Esperando transferencia de {round(cantidad, 2)}€ a la cuenta terminada en {self.__iban[-4:]}')
        return True