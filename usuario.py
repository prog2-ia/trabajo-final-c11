class Usuario:
    def __init__(self, id_usuario, nombre, email, saldo_inicial):#
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.carrito = []
        self.productos_propios = []
        self.historial_pedidos = []
        #atributos privados
        self.email = email
        self.saldo = saldo_inicial
# Getter para retornar el correo electrónico almacenado de forma privada.
    @property
    def email(self):
        return self.__email
# Setter que solo permite correos de gmail o hotmail
    @email.setter
    def email(self, nuevo_email):
        if '@gmail.com' in nuevo_email or '@hotmail.com' in nuevo_email:
            self.__email = nuevo_email
        else:
            print(f'Error: El email "{nuevo_email}" no tiene un formato válido.')
            self.__email = None
# Getter que devuelve el saldo del usuario
    @property
    def saldo(self):
        return self.__saldo
# Setter que se asegura de que no haya un saldo negativo
    @saldo.setter
    def saldo(self, cantidad):
        self.__saldo = max(0, cantidad)

    def __str__(self):
        return f'Usuario {self.id_usuario}: {self.nombre} | Email: {self.email} | Saldo: {self.saldo}€'

    def __repr__(self):
        return f'Usuario({self.id_usuario}, "{self.nombre}", "{self.email}", {self.saldo})'

