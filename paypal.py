from metodo_pago import MetodoPago

class PayPal(MetodoPago):#
    def __init__(self, titular, email):
        super().__init__(titular)
        self.email = email

    def procesar_pago(self, cantidad):
        print(f'Cobrando {round(cantidad, 2)}€ a la cuenta PayPal: {self.email}')
        return True