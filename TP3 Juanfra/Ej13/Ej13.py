# NumPy es una librería fundamental en Python para el cálculo numérico, especialmente útil para trabajar con matrices y arrays
# multidimensionales. Proporciona herramientas eficientes para realizar operaciones matemáticas y manipulaciones de datos.

# CREACION DE ARRAYS
import numpy as np

# Crear un array unidimensional
array_1d = np.array([1, 2, 3, 4, 5])
print("Array 1D:", array_1d)

# Crear un array bidimensional (matriz)
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("Array 2D:\n", array_2d)


# Propiedades de los Arrays

# Los arrays de NumPy tienen varias propiedades útiles:
# Forma: La forma del array (dimensiones).
# Tamaño: El número total de elementos.
# Tipo de dato: Tipo de datos de los elementos.


print("Forma del array 2D:", array_2d.shape)  # (2, 3)
print("Tamaño del array 2D:", array_2d.size)  # 6
print("Tipo de dato del array 2D:", array_2d.dtype)  # int64


# Operaciones Básicas

# Sumar 10 a cada elemento
array_sumado = array_1d + 10
print("Array sumado:", array_sumado)

# Multiplicación por un escalar
array_multiplicado = array_1d * 2
print("Array multiplicado:", array_multiplicado)

# Operaciones entre matrices
array_a = np.array([[1, 2], [3, 4]])
array_b = np.array([[5, 6], [7, 8]])

# Suma de matrices
array_suma = array_a + array_b
print("Suma de matrices:\n", array_suma)

# Producto de matrices
array_producto = np.dot(array_a, array_b)
# Para matrices de mas de 2 dimensiones es preferible usar la funcion np.matmul
print("Producto de matrices:\n", array_producto)

# Funciones de NumPy
print("Media del array 1D:", np.mean(array_1d))
print("Suma del array 1D:", np.sum(array_1d))
print("Máximo del array 1D:", np.max(array_1d))

# Indexación y Slicing

# Acceder al primer elemento
print("Primer elemento del array 1D:", array_1d[0])

# Slicing en un array 1D
print("Elementos del índice 1 al 3:", array_1d[1:4])

# Slicing en un array 2D
print("Primera fila del array 2D:", array_2d[0])
print("Elemento en la fila 1, columna 2:", array_2d[1, 2])
