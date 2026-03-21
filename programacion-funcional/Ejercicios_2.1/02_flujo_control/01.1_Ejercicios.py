###
# EJERCICIOS
###

from os import system
if system("clear") != 0: system("cls")

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

print("=" * 50)
print("EJERCICIO 1: Mayor de dos numeros")
print("=" * 50)

num1 = float(input("Introduce el primer numero: "))
num2 = float(input("Introduce el segundo numero: "))

if num1 > num2:
    print(f"El numero {num1} es mayor que {num2}")
elif num1 < num2:
    print(f"El numero {num2} es mayor que {num1}")
else:
    print(f"Los numeros {num1} y {num2} son iguales")

# Ejercicio 2: Calculadora simple
# Pide al usuario dos numeros y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

print("=" * 50)
print("EJERCICIO 2: Calculadora simple")
print("=" * 50)

num1 = float(input("Introduce el primer numero: "))
num2 = float(input("Introduce el segundo numero: "))
operacion = input("Introduce la operación (+, -, *, /): ")

if operacion == "+":
    resultado = num1 + num2
    print(f"Resultado: {num1} + {num2} = {resultado}")
elif operacion == "-":
    resultado = num1 - num2
    print(f"Resultado: {num1} - {num2} = {resultado}")
elif operacion == "*":
    resultado = num1 * num2
    print(f"Resultado: {num1} * {num2} = {resultado}")
elif operacion == "/":
    if num2 == 0:
        print("Error: No se puede dividir entre cero")
    else:
        resultado = num1 / num2
        print(f"Resultado: {num1} / {num2} = {resultado}")
else:
    print("Operación no válida. Usa +, -, *, o /")


# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero
#  no por 400.

print("=" * 50)
print("EJERCICIO 3: Año bisiesto")
print("=" * 50)

anio = int(input("Introduce un año: "))

# Un año es bisiesto si:
# - Es divisible por 4 Y
# - (NO es divisible por 100 O es divisible por 400)

if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
    print(f"El año {anio} es bisiesto")
else:
    print(f"El año {anio} NO es bisiesto")


###
# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebe (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)
###

print("=" * 50)
print("EJERCICIO 4: Categorizar edades")
print("=" * 50)

edad = int(input("Introduce una edad: "))

if edad >= 0 and edad <= 2:
    print(f"Edad {edad} años: Bebe")
elif edad >= 3 and edad <= 12:
    print(f"Edad {edad} años: Niño")
elif edad >= 13 and edad <= 17:
    print(f"Edad {edad} años: Adolescente")
elif edad >= 18 and edad <= 64:
    print(f"Edad {edad} años: Adulto")
elif edad >= 65:
    print(f"Edad {edad} años: Adulto mayor")
else:
    print("Edad no valida")