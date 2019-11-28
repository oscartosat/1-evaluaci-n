#En este programa le pedimos al usuario
#que teclee los coeficientes de un polinomio
#y hallamos el valor de las raices
def ecuacion():
    print "Introduzca los coeficientes de el polinomio"
    print "A*x^2+B*x+C=0"
    a=input("A= ")
    b=input("B= ")
    c=input("C= ")
    suma=b*b-4*a*c
    raiz1=(-b+(b*b-4*a*c)^(1/2))/(2*a)
    raiz2=(-b-(b*b-4*a*c)^(1/2))/(2*a)
    print "primera solucion= " + raiz1
    print "segunda solucion= " + raiz2

ecuacion()
    

