"""
/*
 * Escribe una función que calcule y retorne el factorial de un número dado
 * de forma recursiva.
 */
"""

def factorial(num:int)->int:
    if num<=1:
        return 1
    else: return num * factorial(num-1)

numero = int(input("Diga un numero: "))

print(f"El factorial del numero es: {factorial(numero)}")