"""
/*
 * Crea una función que reciba dos cadenas como parámetro (str1, str2)
 * e imprima otras dos cadenas como salida (out1, out2).
 * - out1 contendrá todos los caracteres presentes en la str1 pero NO
 *   estén presentes en str2.
 * - out2 contendrá todos los caracteres presentes en la str2 pero NO
 *   estén presentes en str1.
 */
"""

def diferenciador(cadena1:str,cadena2:str)->tuple[str,str]:
    out1 = []
    out2 = []

    for char in cadena1:
        if char not in cadena2:
            out1.append(char)
    for char in cadena2:
        if char not in cadena1:
            out2.append(char)

    return ''.join(out1),''.join(out2)

cadena1 = input("Ingrese la primera cadena: ")
cadena2 = input("Ingrese la segunda cadena: ")

dif1,dif2 = diferenciador(cadena1,cadena2)

print(f"Caracteres presentes en la primera cadena pero no en la segunda: {dif1}")
print(f"Caracteres presentes en la segunda cadena pero no en la primera: {dif2}")