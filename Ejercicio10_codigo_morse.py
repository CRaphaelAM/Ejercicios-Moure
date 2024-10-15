"""
/*
 * Crea un programa que sea capaz de transformar texto natural a código
 * morse y viceversa.
 * - Debe detectar automáticamente de qué tipo se trata y realizar
 *   la conversión.
 * - En morse se soporta raya "—", punto ".", un espacio " " entre letras
 *   o símbolos y dos espacios entre palabras "  ".
 * - El alfabeto morse soportado será el mostrado en
 *   https://es.wikipedia.org/wiki/Código_morse.
 */
"""

def leer_morse(codigo_morse:str)->str:
    alfabeto_morse = {
        '.-': 'A',    '-...': 'B',  '-.-.': 'C',  '-..': 'D',   '.': 'E',
        '..-.': 'F',  '--.': 'G',   '....': 'H',  '..': 'I',    '.---': 'J',
        '-.-': 'K',   '.-..': 'L',  '--': 'M',    '-.': 'N',    '---': 'O',
        '.--.': 'P',  '--.-': 'Q',  '.-.': 'R',   '...': 'S',   '-': 'T',
        '..-': 'U',   '...-': 'V',  '.--': 'W',   '-..-': 'X',  '-.--': 'Y',
        '--..': 'Z',

        '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
        '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',

        '.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': "'", '-.-.--': '!', 
        '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&', '---...': ':', 
        '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_', 
        '.-..-.': '"', '...-..-': '$', '.--.-.': '@', '/': ' '
    }   
    
    traduccion = []


    codigo_morse = codigo_morse.split("  ")

    for ch in codigo_morse:
        ch = ch.split(" ")
        palabra = [alfabeto_morse[char] if char in alfabeto_morse else "?" for char in ch]
        traduccion.append("".join(palabra))

    return " ".join(traduccion)


def leer_palabra(palabra:str)->str:
    alfabeto = {
        'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.',
        'F': '..-.',  'G': '--.',   'H': '....',  'I': '..',    'J': '.---',
        'K': '-.-',   'L': '.-..',  'M': '--',    'N': '-.',    'O': '---',
        'P': '.--.',  'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
        'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',  'Y': '-.--',
        'Z': '--..',

        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',

        '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', 
        '/': '-..-.',  '(': '-.--.',  ')': '-.--.-', '&': '.-...', ':': '---...', 
        ';': '-.-.-.', '=': '-...-',  '+': '.-.-.',  '-': '-....-', '_': '..--.-', 
        '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
    }


def main():
    
    entrada = input("Ingrese la secuencia de caracteres, puede ser código morse o no: ")
    es_morse = True
    for ch in entrada:
        if ch not in("-","."," "):
            es_morse = False
            break

    if es_morse:
        traduccion = leer_morse(entrada)
    else: traduccion = leer_palabra(entrada)

    print(f"La traduccion del codigo escrito: \n{entrada} -> {traduccion}")


if __name__ == "__main__":
    main()