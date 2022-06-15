# Ejercicio 2 (30 puntos): Escriba un programa que pida dos palabras y diga si riman o no. 
# Si coinciden las últimas tres letras tiene que decir que riman. Si coinciden sólo las últimas dos tiene que decir que riman un poco. 
# Y si no coinciden, decir que no riman. Validar que las palabras tengan al menos tres letras. Nota: Utilizar slices

def main():
    palabra1=input("ingrese la primera palabra, que tenga al menos 3 letras: ")
    palabra2=input("ingrese la segunda palabra, que tenga al menos 3 letras: ")
    if len(palabra1)>=3 and len(palabra2)>=3:
        corte=len(palabra1)-3
        corte2=len(palabra1)-2
        recorte=len(palabra2)-3
        recorte2=len(palabra2)-2

        if palabra1[corte:len(palabra1)]==palabra2[recorte:len(palabra2)]:
            print("las palabras escogidas riman")
        elif palabra1[corte2:len(palabra1)]==palabra2[recorte2:len(palabra2)]:
            print("las palabras escogidas riman un poco")
        else:
            print("las palabras escogidas no riman nada")
    else:
        print("al menos una palabra no cumple con los requisitos")
    print(palabra1[0:len(palabra1)])
if __name__=='__main__':
    main()