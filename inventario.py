import copy
from producto import Producto


class Inventario:
    def __init__(self):
        self.__productos = []

    # Getter para permitir el acceso controlado a la lista de productos desde fuera.
    @property
    def productos(self):
        return self.__productos

    # Añade un producto al inventario (Método tradicional)
    def agregar_producto(self, producto):
        if isinstance(producto, Producto):
            if producto not in self.__productos:
                self.__productos.append(producto)
                print(f'Producto "{producto.nombre}" añadido.')
            else:
                print(f'Error: El producto "{producto.nombre}" ya está en el inventario.')
        else:
            print('Error: Solo se pueden añadir objetos de tipo "Producto".')

    # Calcula el valor total del inventario
    def valor_total(self):
        return sum(prod.precio() for prod in self.__productos)

    def detectar_repetidos(self):
        repetidos = []
        vistos = []
        for prod in self.__productos:
            if prod in vistos and prod not in repetidos:
                repetidos.append(prod)
            else:
                vistos.append(prod)
        return repetidos

    def __len__(self):
        return len(self.__productos)

    def __bool__(self):
        return len(self.__productos) > 0

    def __add__(self, otro):
        # Operador + : Crea una NUEVA instancia sin modificar la actual.
        nuevo_inventario = Inventario()
        # Copiamos la lista actual a la nueva instancia
        nuevo_inventario._Inventario__productos = self.__productos.copy()

        if isinstance(otro, Producto):
            if otro in nuevo_inventario._Inventario__productos:
                print(f'Error (+): El producto "{otro.nombre}" ya está en el inventario (no duplicar).')
            else:
                nuevo_inventario._Inventario__productos.append(copy.deepcopy(otro))
        elif isinstance(otro, Inventario):
            # Por si quieres sumar dos inventarios
            for prod in otro.productos:
                if prod not in nuevo_inventario._Inventario__productos:
                    nuevo_inventario._Inventario__productos.append(copy.deepcopy(prod))

        return nuevo_inventario

    def __iadd__(self, otro):
        # Operador += : Modifica la instancia ACTUAL.
        if isinstance(otro, Producto):
            if otro in self.__productos:
                print(f'Error (+=): El producto "{otro.nombre}" ya está en el inventario (no duplicar).')
            else:
                self.__productos.append(otro)
        return self

    def __sub__(self, otro):
        # Operador - : Crea una NUEVA instancia sin modificar la actual.
        nuevo_inventario = Inventario()
        nuevo_inventario._Inventario__productos = self.__productos.copy()

        if isinstance(otro, Producto):
            if otro not in nuevo_inventario._Inventario__productos:
                print(f'Error (-): El producto "{otro.nombre}" no existe en el inventario.')
            else:
                nuevo_inventario._Inventario__productos.remove(otro)

        return nuevo_inventario

    def __isub__(self, otro):
        # Operador -= : Modifica la instancia ACTUAL.
        if isinstance(otro, Producto):
            if otro not in self.__productos:
                print(f'Error (-=): El producto "{otro.nombre}" no existe en el inventario.')
            else:
                self.__productos.remove(otro)
        return self