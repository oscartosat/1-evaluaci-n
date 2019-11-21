def piramide2():
    espacios=" "
    asteriscos="*"
    filas=input("Escribe una altura: ")
    for i in range (1,filas+1):
            print (i*espacios)+((filas-i)*2-1)*asteriscos
piramide2()
