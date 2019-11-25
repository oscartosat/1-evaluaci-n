def ejercicio_16():
    a=input ("Escriba la cantidad de dinero: ")
    billete=input ("Escriba el billete usado: ")
    if 5<a<500:
        if a<billete:
            cambio=billete-a
            print cambio
            if cambio-500>0:
                b=cambio/500
                print "Cambio",b,"billetes de 500"
            if cambio-200>0:
                c=cambio/200
                print "Cambio",c,"billetes de 200"
            if (cambio-200*c)-100>0:
                c2=cambio-200*c
                d=c2/100
                print "Cambio",d,"billetes de 100"
            if (cambio-100*d)-50>0:
                c3=c2-100*d
                e=c3/50
                print "Cambio",e,"billetes de 50"
            if (cambio-50*e)-20>0:
                c4=c3-50*e
                f=c4/20
                print "Cambio",f,"billetes de 20"
            if (cambio-20*f)-10>0:
                c5=c4-20*f
                g=c5/10
                print "Cambio",g,"billetes de 10"
            if (cambio-10*g)-5>0:
                c6=c5-10*g
                h=c6/5
                print "Cambio",h,"billetes de 5"
            if (cambio-5*h)-2>0:
                c7=c6-5*h
                i=c7/2
                print "Cambio",i,"monedas de 2"
            if (cambio-2*i)-1>0:
                c8=c7-2*i
                j=c8/1
                print "Cambio",j,"monedas de 1 euro"
           

        else:
            print "Debe depositar mas dinero o dejar el producto e irse"
                
        
            
ejercicio_16()
