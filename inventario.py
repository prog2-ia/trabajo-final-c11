import copy
from producto import Producto

class Inventario:
    def __init__(self):
        self.__productos = []
# Getter para permitir el acceso controlado a la lista de productos desde fuera.
    @property
    def productos(self):
        return self.__productos
# Añade un producto al inventario
    def agregar_producto(self, producto):
        if isinstance(producto, Producto):
            self.__productos.append(producto)
            print(f'Producto "{producto.nombre}" añadido.')
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

    def __add__(self, nuevo_producto):
        nuevo_inventario = Inventario()
        nuevo_inventario._Inventario__productos = copy.deepcopy(self.__productos)

        if isinstance(otro, Inventario):
            nuevo_inventario._Inventario__productos.extend(copy.deepcopy(otro.productos))
        elif isinstance(otro, Producto):
            nuevo_inventario._Inventario__productos.append(copy.deepcopy(otro))

        return nuevo_inventario