"""
Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en la que el siguiente siempre es la suma de los dos anteriores.
    0, 1, 1, 2, 3, 5, 8, 13...

"""

def main()->None:
    
    rango:int = 50
    anterior:int = 0
    actual:int = 1

    for n in range(rango):  
        """
        if actual == 0 :
            print("0 1", end=" ")
            actual += 1
        else:
            actual,anterior = actual + anterior,actual
            print(actual, end = " ")
"""
        print(anterior, end = " ")
        actual,anterior = actual + anterior,actual
    




if __name__ == "__main__":
    main()