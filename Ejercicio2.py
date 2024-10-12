"""
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.

"""
def es_anagrama(palabra1:str, palabra2:str)->bool:
    """
    Funcion que determina si dos palabras son anagramas.

    Recibe como parametros las dos palabras

    Devuelve bool
    """
    if palabra1 == palabra2: return False

    if len(palabra1) != len(palabra2):
        return False

    for char in palabra1:
        if palabra2.count(char) != 1:
            return False
    return True


def main():
    
    palabra1 = input("Ingrese la primera palabra: ")
    palabra2 = input("Ingrese la segunda palabra: ")

    if es_anagrama(palabra1,palabra2):
        print(f"Resultado: {palabra1} y {palabra2} son anagramas.")
    else: print(f"Resultado: {palabra1} y {palabra2} no son anagramas.")

if __name__ == "__main__":
    main()