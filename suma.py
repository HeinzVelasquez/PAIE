archivo=open("Suma.txt", "a")
def suma():
    n=int(input("Ingrese un numero: "))
    s=0
    for i in range(n+1):
        s+=i

    s1=str(s)

    print ("La suma de 0 hasta ", n, "es", s)
    archivo.write("La suma de 0 hasta " + 'n=% s' %n + " es " + 's=% s' %s +'\n')

#continuar
continua=True
while (continua):
    seleccion=suma()
    print("¿Quieres continuar (s/n)? ")
    if (input ()=="s" or input ()=="S"):
        continua=True
    else:
        continua=False
        print("Fin del programa")

archivo.close ()
