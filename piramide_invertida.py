def piramide_invertida():
    filas=input("Dime la altura de la piramide: ")
    espacios=' '
    asteriscos='*'
    for i in range(filas):
        for nespacios in range(i+1):
            espacios=espacios+" "
        for nasteriscos in range((filas-i)*2-2):
            asteriscos=asteriscos+"*"   
        print espacios+asteriscos
        espacios=" "
        asteriscos="*"
piramide_invertida()
