import copy
from typing import List, Any, Union
from producto import Producto
from excepciones import ProductoNoEncontradoException, ProductoDuplicadoException

class Inventario:
    def __init__(self) -> None:
        self.__productos: List[Producto] = []

    @property
    def productos(self) -> List[Producto]:
        return self.__productos

    # Implementación del Protocolo de Secuencia (__getitem__ y __len__)
    def __getitem__(self, index: int) -> Producto:
        try:
            return self.__productos[index]
        except IndexError:
            raise IndexError('El índice solicitado está fuera del rango del inventario.')

    def __len__(self) -> int:
        return len(self.__productos)

    def __bool__(self) -> bool:
        return len(self.__productos) > 0

    def agregar_producto(self, producto: Producto) -> None:
        if not isinstance(producto, Producto):
            raise TypeError('Solo se pueden añadir objetos de tipo "Producto".')

        if producto in self.__productos:
            raise ProductoDuplicadoException(f'El producto "{producto.nombre}" ya está en el inventario.')

        self.__productos.append(producto)
        print(f'Producto "{producto.nombre}" añadido.')

    def valor_total(self) -> float:
        return float(sum(prod.precio() for prod in self.__productos))

    def detectar_repetidos(self) -> List[Producto]:
        repetidos: List[Producto] = []
        vistos: List[Producto] = []
        for prod in self.__productos:
            if prod in vistos:
                if prod not in repetidos:
                    repetidos.append(prod)
            else:
                vistos.append(prod)
        return repetidos

    def __add__(self, otro: Union[Producto, 'Inventario']) -> 'Inventario':
        nuevo_inventario = Inventario()
        nuevo_inventario.__productos = self.__productos.copy()

        if isinstance(otro, Producto):
            if otro in nuevo_inventario.__productos:
                raise ProductoDuplicadoException(f'Error (+): El producto "{otro.nombre}" ya está en el inventario.')
            nuevo_inventario.__productos.append(copy.deepcopy(otro))
        elif isinstance(otro, Inventario):
            for prod in otro:
                if prod not in nuevo_inventario.__productos:
                    nuevo_inventario.__productos.append(copy.deepcopy(prod))
        return nuevo_inventario

    def __iadd__(self, otro: Producto) -> 'Inventario':
        if isinstance(otro, Producto):
            if otro in self.__productos:
                raise ProductoDuplicadoException(f'Error (+=): El producto "{otro.nombre}" ya está.')
            self.__productos.append(otro)
        return self

    def __sub__(self, otro: Producto) -> 'Inventario':
        nuevo_inventario = Inventario()
        nuevo_inventario.__productos = self.__productos.copy()

        if isinstance(otro, Producto):
            if otro not in nuevo_inventario.__productos:
                raise ProductoNoEncontradoException(f'Error (-): "{otro.nombre}" no existe en el inventario.')
            nuevo_inventario.__productos.remove(otro)
        return nuevo_inventario

    def __isub__(self, otro: Producto) -> 'Inventario':
        if isinstance(otro, Producto):
            if otro not in self.__productos:
                raise ProductoNoEncontradoException(f'Error (-=): "{otro.nombre}" no existe en el inventario.')
            self.__productos.remove(otro)
        return self