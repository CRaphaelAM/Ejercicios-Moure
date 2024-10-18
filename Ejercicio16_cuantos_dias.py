"""
/*
 * Crea una función que calcule y retorne cuántos días hay entre dos cadenas
 * de texto que representen fechas.
 * - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
 * - La función recibirá dos String y retornará un Int.
 * - La diferencia en días será absoluta (no importa el orden de las fechas).
 * - Si una de las dos cadenas de texto no representa una fecha correcta se
 *   lanzará una excepción.
 */
"""

from datetime import date,timedelta

def calcular_dias(fecha1:str,fecha2:str)->int:
    error = "Formato de fecha incorrecto"
    if len(fecha1) != 10 or len(fecha2) != 10:
        raise(Exception(error))
    
    f1 = fecha1.split('/')
    f2 = fecha2.split('/')

    for n in range(3):
        if not f1[n].isdigit() or not f2[n].isdigit():
            raise(Exception(error))
        else: 
            f1[n] = int(f1[n])
            f2[n] = int(f2[n])
    if f1[0] not in range(1,32) or f2[0] not in range(1,32) or f1[1] not in range(1,13) or f2[1] not in range(1,13):
        raise(Exception(error))
    
    date1 = date(f1[2],f1[1],f1[0])
    date2 = date(f2[2],f2[1],f2[0])
    
    return abs((date1 - date2).days)

def main():
    print("Debe ingresar las fechas en formato  'dd/MM/yyyy'")
    fecha1 = input("Ingrese la primera fecha: ")
    fecha2 = input("Ingrese la segunda fecha: ")
    try:
        dias = calcular_dias(fecha1,fecha2)
        print(f"Cantidad de dias entre ambas fechas: {dias}")
    except Exception as E:
        print(f"Programa abortado debido a: {E}")

if __name__ == '__main__':
    main()