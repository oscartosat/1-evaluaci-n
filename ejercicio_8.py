#Escriba una funcion que reciba un precio y el tipo de IVA aplicable
#(general 16%, reducido 7% y superreducido 4%) y devuelva el precio mas IVA.
#Por ejemplo, si recibe 100 y "reducido" debería devolver 116.
def ejercicio_8():
    a=input ("introduzca precio: ")
    b=raw_input ("introduzca tipo iva: ")
    if b=="g":
        print a+(a*0.16)
    if b=="r":
        print a+(a*0.07)
    if b=="s":
        print a +(a*0.04)

ejercicio_8()
