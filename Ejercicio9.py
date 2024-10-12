"""
/*
 * Crea un programa se encargue de transformar un número
 * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
 *
"""

n = int(input("Ingrese el numero que desea convertir a binario: "))
binario = ""
while n > 0:

    mod = n % 2
    div = n //2
    n = div
    binario+=str(mod)
binario = binario[::-1]
print(binario)