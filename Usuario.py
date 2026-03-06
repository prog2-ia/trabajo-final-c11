class Usuario:
    def __init__(self, id_usuario, nombre, email, saldo_inicial):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.carrito = []
        self.productos_propios = []
        self.historial_pedidos = []
        #atributos privados
        self.email = email
        self.saldo = saldo_inicial

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, nuevo_email):
        if '@gmail.com' in nuevo_email or '@hotmail.com' in nuevo_email:
            self.__email = nuevo_email
        else:
            print(f'Error: El email '{nuevo_email}' no tiene un formato válido.')
            self.__email = None

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, cantidad):
        if cantidad < 0:
            print('Error: El saldo no puede ser negativo. Se asignará 0€ por seguridad.')
            self.__saldo = 0
        else:
            self.__saldo = cantidad

    def __str__(self):
        return f'Usuario {self.id_usuario}: {self.nombre} | Email: {self.email} | Saldo: {self.saldo}€')

