def contador():
    print "Introduzca el numero"
    a=input("numero= ")
    for i in range (1,a+1):
        if (a % 2 == 0):
            print "i= ", i, "este numero es par"
        else:
            print "i= ", i, "este numero es impar"
contador()
