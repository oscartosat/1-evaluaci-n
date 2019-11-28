#En este programa le pedimos al usuario que introduzdca un numero
#el programa primero le responde si es par o impar y posteriormente
#si el numero es multiplo de 3 o no
def multiplo():
    a=input ("Escribe un numero: ")
    if a%2==0:
        print a, "El numero es par"
    else:
        print a, "El numero es impar"
    if a%3==0:
        print a, "El numero es multiplo de 3"
    else:
        print a, "El numero no es multiplo de 3"

multiplo()
