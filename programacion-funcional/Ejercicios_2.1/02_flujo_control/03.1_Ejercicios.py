###
#EJERCICIOS
###

from os import system
if system("clear") != 0: system("cls")

###
# Ejercicio 1: El mensaje secreto
# Dada la siguiente lista:
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenacion, crea una nueva lista que contenga solo el
# mensaje "secreto".
###

print("=" * 50)
print("EJERCICIO 1: El mensaje secreto")
print("=" * 50)

mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]

print("\nLista original:")
print(mensaje)

# Usando slicing y concatenación
parte1 = mensaje[7:10]   # ['s', 'e', 'c']
parte2 = mensaje[10:]    # ['r', 'e', 't', 'o']

secreto = parte1 + parte2

print("\nMensaje secreto (lista):")
print(secreto)

print("\nMensaje secreto (texto):")
print("".join(secreto))


# Ejercicio 2: Intercambio de posiciones
# Dada la siguiente lista:
# numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la ultima posicion utilizando solo asignacion por indice.
print("=" * 50)
print("EJERCICIO 2: Intercambio de posiciones")
print("=" * 50)

numeros = [10, 20, 30, 40, 50]

print("\nLista original:")
print(numeros)

temp = numeros[0]
numeros[0] = numeros[-1]
numeros[-1] = temp

print("\nLista modificada:")
print(numeros)



# Ejercicio 3: El sandwich de listas
# Dadas las siguientes listas:
# pan = ["pan arriba"]
# ingredientes = ["jamon", "queso", "tomate"]
# pan_abajo = ["pan abajo"]
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes
# y el pan de abajo, en ese orden.

print("=" * 50)
print("EJERCICIO 3: El sandwich de listas")
print("=" * 50)



pan = ["pan arriba"]
ingredientes = ["jamon", "queso", "tomate"]
pan_abajo = ["pan abajo"]

sandwich = pan + ingredientes + pan_abajo

print("\nSandwich:")
print(sandwich)



# Ejercicio 4: Duplicando la lista
# Dada una lista:
# lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]

print("=" * 50)
print("EJERCICIO 4: Duplicando la lista")
print("=" * 50)

lista = [1, 2, 3]

duplicada = lista + lista

print("\nLista duplicada:")
print(duplicada)


# Ejercicio 5: Extrayendo el centro
# Dada una lista con un numero impar de elementos, extrae el elemento que se
# encuentra en el centro de la lista utilizando slicing.
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30

print("=" * 50)
print("EJERCICIO 5: Extrayendo el centro")
print("=" * 50)


lista = [10, 20, 30, 40, 50]

centro = lista[len(lista)//2 : len(lista)//2 + 1]

print("\nElemento central:")
print(centro)


# Ejercicio 6: Reversa parcial
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenacion).
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]

print("=" * 50)
print("EJERCICIO 6: Reversa parcial")
print("=" * 50)


lista = [1, 2, 3, 4, 5, 6]

mitad = len(lista) // 2

primera_parte = lista[:mitad][::-1]
segunda_parte = lista[mitad:]

resultado = primera_parte + segunda_parte

print("\nLista resultante:")
print(resultado)