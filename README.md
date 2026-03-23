# Sistema de Gestión de Coleccionismo (Cromos y Figuras)
## 1. Propósito del proyecto
El objetivo principal de este proyecto es permitir a los usuarios gestionar sus colecciones de artículos (cromos y figuras), calcular el valor de su inventario en base al estado de conservación y la rareza, y procesar transacciones (pedidos e intercambios).

El sistema aplica los conceptos vistos en la asignatura:
* **Encapsulamiento:** Protección de datos sensibles (saldo, email, estado de los artículos) mediante propiedades (`@property`) y validadores (`.setter`).
* **Herencia y Polimorfismo:** Uso de jerarquías de clases (ej. `Cromos` y `Figura` heredan de `Producto`) y métodos polimórficos para procesar diferentes métodos de pago (`PayPal`, `Tarjeta`, `Transferencia`).
* **Clases Abstractas:** Definición de interfaces comunes usando el módulo `abc` para garantizar que las subclases implementen métodos clave como `precio()` o `ejecutar()`.
* **Sobrecarga de Operadores:** Implementación de métodos mágicos (`__add__`, `__eq__`) para combinar inventarios y detectar artículos repetidos.

## 2. Instalación
Para instalar este proyecto sigue estos pasos:
1. **Clona el repositorio** en tu equipo local:
   ```bash
   git clone https://github.com/prog2-ia/trabajo-final-c11

## 3. Uso
Para ejecutar el sistema abre el archivo main.py
