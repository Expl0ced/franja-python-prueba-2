# Ejercicio 1 (30 puntos): Escribir un programa que contenga
# una función que reciba una lista de palabras y devuelva la más larga. 
# Imprimir por pantalla la palabra resultante

def lista_palabra():
    palabra=["algodon", "corindon", "pistola", "paralelepipedo"]
    comodin=palabra[0]
    for i in range(0,len(palabra)):
        if len(comodin)<len(palabra[i]):
            comodin=palabra[i]
    return print(comodin)
            


def main():
    lista_palabra()



if __name__=='__main__':
    main()
