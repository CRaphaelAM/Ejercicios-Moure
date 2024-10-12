"""
Crea una única función (importante que sólo sea una) que sea capaz
de calcular y retornar el área de un polígono.
- La función recibirá por parámetro sólo UN polígono a la vez.
- Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
- Imprime el cálculo del área de un polígono de cada tipo.

"""

from math import sqrt

class Poligono:
    pass

class Triangulo(Poligono):
    def __init__(self,a:float, b:float, c:float):
        super().__init__()
        self.lado_a = a
        self.lado_b = b
        self.lado_c = c
    def calcular_perimetro(self)->float:
        return self.lado_a + self.lado_b + self.lado_c
    
    def calcular_area(self) -> float:
        
        semiperimetro = self.calcular_perimetro()/2
    
        return sqrt(semiperimetro*(semiperimetro - self.lado_a)*(semiperimetro - self.lado_b)*(semiperimetro - self.lado_c))

class Cuadrilatero(Poligono):
    def __init__(self,base:float, altura:float):
        super().__init__()
        self.base = base
        self.altura = altura
        
    def calcular_area(self) -> float:
    
        return self.base * self.altura



def main() -> None:
    
    triangulo = Triangulo(4,5,3)
    cuadrado = Cuadrilatero(4,4)
    rectangulo = Cuadrilatero(4,5)

    print(triangulo.calcular_area())
    print(triangulo.calcular_perimetro()/2)
    print(cuadrado.calcular_area())

if __name__ == "__main__":
    main()