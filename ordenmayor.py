archivo=open("Mayor.txt", "a")
def mayor ():
    n=int(input("Ingrese un número: "))
    m=int(input ("Ingrese un segundo número: "))

    if ( n>m):
        mayor=[i for i in range (n,m, -1)]
        print( mayor)
        archivo.write('mayor =% s' %mayor + '\n')
    else:
        mayor=[i for i in range (m,n,-1)]
        print (mayor)
        archivo.write('mayor=% s' %mayor + '\n')

#continuar
continuar=True
while (continuar):
    seleccion=mayor()
    print("¿Desea continuar (s/n)? ")
    if (input ()=="s" or input ()=="S"):
        continuar=True
    else:
        continuar=False
        print("Fin del programa")

archivo.close ()
