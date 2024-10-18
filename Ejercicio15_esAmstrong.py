"""
/*
 * Escribe una función que calcule si un número dado es un número de Armstrong
 * (o también llamado narcisista).
 * Si no conoces qué es un número de Armstrong, debes buscar información
 * al respecto.
 */
"""

def es_amstrong(numero:str)->bool:
    suma = 0
    exp = len(numero)
    for n in numero:
        suma+= int(n)**exp

    return suma == int(numero)

def main()->None:
    numero = input("Ingrese el numero a verificar: ")
    if es_amstrong(numero):
        print(f"El numero '{numero}' es amstrong.")
    else: print(f"El numero '{numero}' no es amstrong.")

if __name__ == '__main__':
    main()