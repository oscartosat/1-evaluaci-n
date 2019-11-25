def ejercicio_13():
    filas=input ("Escriba la altura: ")
    espacios=" "
    asteriscos="*"
    for i in range (1,filas+1):
        print (filas-i)*espacios+(i*2-1)*asteriscos
ejercicio_13()
