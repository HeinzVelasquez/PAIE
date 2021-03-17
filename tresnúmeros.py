archivo =open ("tresnumeros.txt", "a")
def funcion ():
    x=int(input("Ingrese el primer número: "))
    y=int(input("Ingrese el segundo número: "))
    z=int(input("Ingrese el tercer número: "))

    if (x > y and x > z):
        suma=x+y+z
        print("La suma de los números es: ",suma)
        archivo.write('suma=% s' %suma + '\n')
    elif (y>x and y >z):
        mult=x*y*z
        print("La multiplicacion de los números es: ",mult)
        archivo.write('mult=% s' %mult + '\n')
    elif (z>x and z>y):
        print("Los números son: ", x, " ", y, " ", z)
        archivo.write('x=% s' %x + " " + 'y=% s' %y + " " + 'z=% s' %z + '\n')
    elif (x==y and x!=z):
        print("El número diferente es: ", z)
        archivo.write("El número diferente es: " + 'z=% s' %z + '\n')
    elif (x==z and x!=y):
        print("El número diferente es: ", y)
        archivo.write("El número diferente es: " + 'y=% s' %y + '\n')
    elif (y==z and y!=x):
        print("El número diferente es: ", x)
        archivo.write("El número diferente es: " + 'x=% s' %x + '\n')
    else:
        print("Los tres números son iguales")
        archivo.write("Los tres números son iguales"+ '\n')

#Menú de continuar
continuar=True
while (continuar):
    seleccion=funcion()
    print("¿Quieres continuar (s/n) ")
    if (input ()== "s" or input ()=="S"):
        continuar=True
    else:
        continuar=False
        print("Fin del programa")

archivo.close ()
