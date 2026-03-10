from metodo_pago import MetodoPago

class PayPal(MetodoPago):
    def __init__(self, titular, email):
        super().__init__(titular)
        self.email = email

    def procesar_pago(self, cantidad):
        print(f'Conectando con PayPal para cobrar {cantidad} euros a la cuenta {self.email}...')
        return True