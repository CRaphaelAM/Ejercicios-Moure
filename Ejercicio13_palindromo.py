"""
/*
 * Escribe una función que reciba un texto y retorne verdadero o
 * falso (Boolean) según sean o no palíndromos.
 * Un Palíndromo es una palabra o expresión que es igual si se lee
  * de izquierda a derecha que de derecha a izquierda.
 * NO se tienen en cuenta los espacios, signos de puntuación y tildes.
 * Ejemplo: Ana lleva al oso la avellana.
 */
"""


def es_palindromo(cadena:str)->bool:
    letras = []

    for char in cadena.lower():
        if char.isalpha():
            letras.append(char)

    letras_reversed = letras[::-1]

    if letras != letras_reversed:
        return False
        
    return True

cadena = input("Ingrese la cadena que desea comprobar: ")
if es_palindromo(cadena):
    print("La cadena ingresada es un palindromo.")
else:
    print("La cadena ingresada no es un palindromo.")