"""
/*
 * Crea un programa que comprueba si los paréntesis, llaves y corchetes
 * de una expresión están equilibrados.
 * - Equilibrado significa que estos delimitadores se abren y cieran
 *   en orden y de forma correcta.
 * - Paréntesis, llaves y corchetes son igual de prioritarios.
 *   No hay uno más importante que otro.
 * - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
 * - Expresión no balanceada: { a * ( c + d ) ] - 5 }
 */
"""

def main():
    caracteres = {
        '[':']',
        '(':')',
        '{':'}'
    }
    stack = []
    expresion  = input("Ingrese su expresion: ")
    correcto = True
    for char in expresion:
        if char in caracteres:
            if expresion.count(char)!= expresion.count(caracteres[char]):
                correcto = False
                break
            stack.append(char)
        elif char in caracteres.values():
            if len(stack) == 0 or caracteres[stack.pop()] != char:
                correcto = False
                break
            
    if len(stack) != 0: correcto = False    
    if correcto:
        print("La expresion ingresada es correcta.")
    else: print("La expresion ingresada no es correcta")

if __name__ == '__main__':
    main()