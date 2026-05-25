import pickle
import os
from typing import List, Optional
from usuario import Usuario
from excepciones import UsuarioDuplicadoException, UsuarioNoEncontradoException

class GestorUsuarios:
    def __init__(self, archivo_datos: str = 'usuarios_db.pickle') -> None:
        self.archivo_datos: str = archivo_datos
        self.usuarios: List[Usuario] = self.cargar_de_fichero()

    def buscar_usuario(self, id_usuario: int) -> Optional[Usuario]:
        for u in self.usuarios:
            if u.id_usuario == id_usuario:
                return u
        return None

    def añadir_usuario(self, usuario: Usuario) -> None:
        if self.buscar_usuario(usuario.id_usuario):
            raise UsuarioDuplicadoException(f'Error al añadir: El usuario con ID {usuario.id_usuario} ya existe.')

        self.usuarios.append(usuario)
        print(f'Usuario {usuario.nombre} añadido correctamente.')
        self.guardar_en_fichero()  # Guardamos automáticamente al añadir

    def sustituir_usuario(self, id_usuario: int, nuevo_usuario: Usuario) -> None:
        for i, u in enumerate(self.usuarios):
            if u.id_usuario == id_usuario:
                self.usuarios[i] = nuevo_usuario
                print(f'Usuario ID {id_usuario} sustituido exitosamente por {nuevo_usuario.nombre}.')
                self.guardar_en_fichero()
                return
        raise UsuarioNoEncontradoException(f'Error al sustituir: No se encontró el usuario con ID {id_usuario}.')

    def eliminar_usuario(self, id_usuario: int) -> None:
        usuario = self.buscar_usuario(id_usuario)
        if usuario:
            self.usuarios.remove(usuario)
            print(f'Usuario con ID {id_usuario} eliminado.')
            self.guardar_en_fichero()
        else:
            raise UsuarioNoEncontradoException(f'Error al eliminar: No se encontró el usuario con ID {id_usuario}.')

    def guardar_en_fichero(self) -> None:
        try:
            with open(self.archivo_datos, 'wb') as f:
                pickle.dump(self.usuarios, f)
        except OSError as e:
            print(f'Advertencia: No se pudo actualizar el archivo binario. Detalle: {e}')

    def cargar_de_fichero(self) -> List[Usuario]:
        # Comprobamos si el fichero existe usando os.path.exists
        if os.path.exists(self.archivo_datos):
            try:
                with open(self.archivo_datos, 'rb') as f:
                    return list(pickle.load(f))
            except (OSError, EOFError, pickle.UnpicklingError) as e:
                print(f'Error al cargar el archivo binario: {e}')
                return []
        return []