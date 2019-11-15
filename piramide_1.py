def piramide_1():
    filas=input("Dime la altura de la piramide: ")
    espacios=' '
    asteriscos='*'
    for i in range(filas):
        for nespacios in range(filas-i-1):
            espacios=espacios+' '
        for nasteriscos in range(1,2*i+1):
            asteriscos=asteriscos+'*'
        print espacios + asteriscos
        espacios=' '
        asteriscos='*'

            

piramide_1()
