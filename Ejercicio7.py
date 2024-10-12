"""
/*
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
 */
"""

cadena = input("Ingrese una cadena: ")
print(cadena[::-1])

for char in cadena[-1:-1*len(cadena) -1:-1]:
    print (char, end="")