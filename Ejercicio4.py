"""
Determinar que numeros son primos entre 1 y 100

"""

def es_primo(n:int)->bool:
    if n == 0 or n == 1: return False
    
    for i in range(2,n):
        if n % i == 0: return False
    return True

def main() ->None:
    for n in range(101):
        if es_primo(n): print(n,end = " ")

if __name__ == "__main__":
    main()