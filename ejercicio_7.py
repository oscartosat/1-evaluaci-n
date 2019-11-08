#En el ejercicio anerior mejorar la funcion para que se evite la division
#por 0. Asi se envian los parametros 7,0,'D' la funciion mostrara
#por pantalla un mensaje de error.
def ejercicio_7():
    a=input ("primer numero: ")
    b=input ("segundo numero: ")
    c=raw_input ("operacion: ")
    if c=="s":
        print a+b 
    if c=="r":
        print a-b
    if c=="m":
        print a*b
    if c=="d":
        if b==0:
            print "error"
            if b==0:
                e=input ("introduzca otro numero: ")
                print a/e
        else:
            print a/b


ejercicio_7()
