#Escriba una función llamada “multiplicación” que reciba como argumento 
#cuatro numeros reales distintos de cero y que devuelva su producto.
def ejercicio_1():
    a=input("Primer factor: ")
    if (a==0):
        a=input("Introduzca otro numero: ")
    b=input("Segundo factor: ")
    if (b==0):
        b=input("Introduzca otro numero: ")
    c=input("Tercer factor: ")
    if (c==0):
        c=input("Introduzca otro numero: ")
    d=input("Cuarto factor: ")
    if (d==0):
        d=input("Introduzca otro numero: ")
    x=a*b*c*d
    print x
    

ejercicio_1()
