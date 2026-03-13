from producto import Producto

class Inventario:
    def __init__(self):
        self.__productos = []

    @property
    def productos(self):
        return self.__productos

    def agregar_producto(self, producto):
        if isinstance(producto, Producto):
            self.__productos.append(producto)
            print(f'Producto "{producto.nombre}" añadido.')
        else:
            print('Error: Solo se pueden añadir objetos de tipo "Producto".')

    def valor_total(self):
        total = 0
        for prod in self.__productos:
            total += prod.precio()
        return total