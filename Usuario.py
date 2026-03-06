class Usuario:
    def __init__(self, id_usuario, nombre, email, saldo):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.email = email
        self.saldo = saldo
        self.carrito = []
        self.productos_propios = []
        self.historial_pedidos = []

    def mostar_informacion(self):
        print('----INFORMACIÓN DEL USUARO----')
        print('ID:', self.id_usuario)
        print('Nombre:', self.nombre)
        print('Email:', self.email)
        print('Saldo:', self.saldo)

    def anyadir_carrito(self, producto):
        self.carrito.append(producto)

    def eliminar_del_carrito(self, producto):
        if producto in self.carrito:
            self.carrito.remove(producto)

    def anyadir_saldo(self, cantidad):
        self.saldo += cantidad

    def validar_email(self):
        if '@gmail.com' in self.email or '@hotmail.com' in self.email:
            return True
        else:
            return False

    if __name__ =='__main__':

        if validar_email():
            print("Email válido")
        else:
            print("Email incorrecto")
