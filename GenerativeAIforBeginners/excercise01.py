# Ejercicio:
# Escribe una función que reciba una lista de números y devuelva otra lista
# con los números pares ordenados de menor a mayor.

def obtener_pares_ordenados(lista_numeros):
    # Filtrar números pares
    pares = [num for num in lista_numeros if num % 2 == 0]
    # Ordenar la lista de números pares
    pares.sort()
    return pares


# Ejemplo de uso:
entrada = [5, 3, 8, 6, 7, 2]
salida = obtener_pares_ordenados(entrada)
print(salida)  # Salida esperada: [2, 6, 8]
