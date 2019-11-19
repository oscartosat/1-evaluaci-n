def pajarita():
    h=input("Escribe un numero impar: ")
    a="*"
    b=" "
    c=((h/2)+1/2)
    for i in range(1,h+1):
        r=(2*i)-1
        s=2*i
        if i<(c+1):
            print (i*a)+((h-s)*b)+(i*a)
        if i==c:
            print h*a
        if i>(c+1):
            print ((h-(i-1))*a)+((s-(h+2))*b)+((h-(i-1))*a)

pajarita()
                    
                                              
