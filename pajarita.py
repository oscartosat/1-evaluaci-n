def pajarita():
    altura=input("Escribe un numero: ")
    asteriscos="*"
    espacios=" "
    medio=((altura/2)+1/2)
    for i in range(1,altura+1):
        if i<(medio+1):
            print (asteriscos*i)+((altura-(2*i))*espacios)+(asteriscos*i)
        if i==medio:
            print asteriscos*altura
        if i>(medio+1):
            print ((altura-(i-1))*asteriscos)+(((2*i)-(altura+2))*espacios)+((altura-(i-1))*asteriscos)
pajarita()
