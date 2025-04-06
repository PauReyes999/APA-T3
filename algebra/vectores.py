"""
    Tercera tarea de APA - manejo de vectores

    Nombre y apellidos: Pau Reyes Boix
"""

"""
Este módulo implementa la clase Vector y permite realizar diversas operaciones vectoriales, como:

- Suma de vectores
- Producto escalar
- Producto de Hadamard
- Componentes tangencial y normal respecto a otro vector

>>> v1 = Vector([1, 2, 3])
>>> v2 = Vector([4, 5, 6])
>>> v1 * 2
Vector([2, 4, 6])
>>> v1 * v2
Vector([4.0, 10.0, 18.0])
>>> v1 @ v2
32
>>> v1 = Vector([2, 1, 2])
>>> v2 = Vector([0.5, 1, 0.5])
>>> v1 // v2
Vector([1.0, 2.0, 1.0])
>>> v1 % v2
Vector([1.0, -1.0, 1.0])
"""

import math

class Vector:
    """
    Clase para representar y manipular vectores de forma sencilla.
    """

    def __init__(self, iterable):
        """
        Inicializa un nuevo vector a partir de cualquier iterable que contenga sus componentes.
        """
        self.vector = [valor for valor in iterable]
        return None  # Instrucción innecesaria, pero permitida

    def __repr__(self):
        """
        Devuelve una representación oficial del vector, útil para depuración y reproducción exacta.
        """
        return 'Vector' 
        
import math

class Vector:
    """
    Clase para manejar vectores de forma sencilla. Permite operar con listas de números como si fueran vectores.
    """

    def __init__(self, iterable):
        """
        Constructor: recibe cualquier cosa iterable (como una lista o tupla) y guarda sus valores como componentes del vector.
        """
        self.vector = [valor for valor in iterable]
        return None  # No hace falta, pero tampoco molesta

    def __repr__(self):
        """
        Representación formal del vector, útil si queremos copiar y pegar para recrearlo igual.
        """
        return 'Vector(' + repr(self.vector) + ')'

    def __str__(self):
        """
        Muestra el vector de forma más limpia, solo los valores.
        """
        return str(self.vector)

    def __getitem__(self, key):
        """
        Permite acceder a un elemento concreto (o varios si se pasa una porción).
        """
        return self.vector[key]

    def __setitem__(self, key, value):
        """
        Permite cambiar una o más componentes del vector con índices.
        """
        self.vector[key] = value

    def __len__(self):
        """
        Devuelve cuántas componentes tiene el vector.
        """
        return len(self.vector)

    def __add__(self, other):
        """
        Suma otro vector o un número. Si es número, lo suma a cada componente.
        """
        if isinstance(other, (int, float, complex)):
            return Vector(uno + other for uno in self)
        else:
            return Vector(uno + otro for uno, otro in zip(self, other))

    __radd__ = __add__

    def __neg__(self):
        """
        Cambia el signo de todas las componentes del vector.
        """
        return Vector([-1 * item for item in self])

    def __sub__(self, other):
        """
        Resta otro vector o número. Usa suma y signo negativo para no repetir código.
        """
        return -(-self + other)

    def __rsub__(self, other):
        """
        Lo mismo que la resta, pero cuando el vector va a la derecha.
        """
        return -self + other
        
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
