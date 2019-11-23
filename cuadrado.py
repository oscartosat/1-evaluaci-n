def cuadrado():
    espacios=" "
    asteriscos="*"
    filas=input("Escriba una altura: ")
    for i in range (1,filas+1):
        if filas%2==0:
            if i<3:
                print filas*asteriscos
            if 3<i<filas/2:
                print (2*asteriscos)+(filas/2-3)*espacios+2*asteriscos+(filas/2-3)*espacios+(2*asteriscos)
            if i==filas/2:
                print filas*asteriscos
            if filas/2<i<filas-2:
                print (2*asteriscos)+(filas/2-3)*espacios+2*asteriscos+(filas/2-3)*espacios+(2*asteriscos)
            if i>filas-2:
                print filas*asteriscos
        else:
            if i<3:
                print (filas+1)*asteriscos
            if 3<i<(filas-1)/2:
                print (2*asteriscos)+(filas/2-2)*espacios+2*asteriscos+(filas/2-2)*espacios+(2*asteriscos)
            if i==(filas-1)/2:
                print (filas+1)*asteriscos
            if filas/2<i<filas-2:
                print (2*asteriscos)+(filas/2-2)*espacios+2*asteriscos+(filas/2-2)*espacios+(2*asteriscos)
            if i>filas-2:
                print (filas+1)*asteriscos
cuadrado()
