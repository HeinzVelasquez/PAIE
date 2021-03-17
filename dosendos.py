archivo=open("CuentaDos.txt", "w")
def cuentados ():
    n=int(input("Ingrese el primer número: "))
    m=int(input("Ingrese el segundo número: "))
    cuenta=0
    for i in range (n,m, 2):
        if i % 2 == 0:
            cuenta= cuenta +1
        print(i)
        archivo.write ('i=% s' %i)
        archivo.write ('\n')
 #programa continua
continua=True
while (continua):
    seleccion=cuentados()
    print("¿Quieres continuar (s/n)? ")
    if (input ()=="s" or input ()=="S"):
        continua=True
    else:
        continua=False
        print("Fin del programa")

archivo.close ()
