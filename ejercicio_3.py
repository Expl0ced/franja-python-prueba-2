# Ejercicio 3 (30 puntos): Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función
def circulo(pi, radio):
    radio=radio**2
    return pi*radio

def cilindro(pi, radio, h):
    return circulo(pi, radio)*h


def main():
    radio=float(input("ingrese un valor para radio: "))
    h=float(input("ingrese un valor para altura: "))
    pi=3.14
    print(circulo(pi, radio))
    print(cilindro(pi, radio, h))

25
if __name__ == '__main__':
    main()