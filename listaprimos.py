#En este programa el programa determina a partir de una lista de
#numeros si estos son primos o no
def primo():
    a=input ("Introduzca el numero: ")
    b=input ("Introduzca el numero: ")
    primo=True
    for i in range (a,b):
        for c in range (2,i-1):
            if (i%c==0):
                primo=False
        if (primo==True):
            print "i= ", i, "El numero es primo"
        else:
            print "i= ", i, "EL numero no es primo"   
        primo=True
        
primo()
