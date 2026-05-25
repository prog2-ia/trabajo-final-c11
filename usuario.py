from  excepciones import EmailInvalidoException
from typing import Any, List
class Usuario:
    def __init__(self, id_usuario: int, nombre: str, email: str, saldo_inicial: float) -> None:
        self.id_usuario: int = id_usuario
        self.nombre: str = nombre
        self.carrito: List[Any] = []
        self.productos_propios: List[Any] = []
        self.historial_pedidos: List[Any] = []
        self.saldo: float = saldo_inicial
        # Asignamos el email al final para que pase por el setter y su validación
        self.email: str = email

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, nuevo_email: str) -> None:
        # Lanzar excepción si el dato no cumple el requisito
        if '@gmail.com' in nuevo_email or '@hotmail.com' in nuevo_email:
            self.__email = nuevo_email
        else:
            raise EmailInvalidoException(f'Error: El email "{nuevo_email}" no tiene un formato válido (solo gmail o hotmail).')

    @property
    def saldo(self) -> float:
        return self.__saldo

    @saldo.setter
    def saldo(self, cantidad) -> None:
        self.__saldo = max(0, cantidad)

    def __str__(self) -> str:
        return f'Usuario {self.id_usuario}: {self.nombre} | Email: {self.email} | Saldo: {self.saldo}€'

    def __repr__(self) -> str:
        return f'Usuario({self.id_usuario}, "{self.nombre}", "{self.email}", {self.saldo})'