"""
/*
 * Crea un programa que cuente cuantas veces se repite cada palabra
 * y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que
 *   lo resuelvan automáticamente.
 */
"""
def main()->None:

    contador = {}

    cadena = input("Ingrese una cadena de texto: ")

    cadena = cadena.lower().split()

    #Recorrer toda la cadena tomando todas las "palabras", pueden tener signos de puntuacion como ","
    for frase in cadena:
        palabra = ""
        #Recorrer cada frase caracter a caracter revisando si hay signos de putuación
        for char in frase:
            if char.isalpha():
                palabra+= char
            else: continue

        contador[palabra] = contador.get(palabra,0) + 1

    for elem in contador:
        print(f"{elem} -> {contador[elem]}")

    n_dict = sorted(contador.keys(), key = lambda x: contador[x], reverse = True)
    print("Diccionario ordenado:")
    print(type(n_dict))
    print(n_dict)

    for elem in n_dict:
        print(f"{elem} -> {contador[elem]}")


if __name__ == "__main__":
    main()