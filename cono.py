archivo=open("Cono.txt", "a")
import math

def cono():
    print("Calculos para el Cono.\n")
    print("1.Area base.\n2.Area lateral.\n3.Area total.\n4.Volumen.\n")
    x=int(input("Escoja una operacion: "))


    if x==1:
        r=float(input("Ingrese el radio del cono: "))
        g=float(input("Ingrese la generatriz del cono: "))
        h=float(input("Ingrese la altura del cono: "))

        abase=math.pi*r**2
        print("El área de la base es: ", abase)
        archivo.write('abase=% s' %abase + '\n')

    if x==2:
        r=float(input("Ingrese el radio del cono: "))
        g=float(input("Ingrese la generatriz del cono: "))
        h=float(input("Ingrese la altura del cono: "))
            
        alateral=math.pi*r*g
        print("El area lateral es: ", alateral)
        archivo.write('alateral=% s' %alateral + '\n')

    if x==3:
        r=float(input("Ingrese el radio del cono: "))
        g=float(input("Ingrese la generatriz del cono: "))
        h=float(input("Ingrese la altura del cono: "))

        atotal=abase+alateral
        print("El área Total es: ", atotal)
        archivo.write('atotal=% s' %atotal + '\n')

    if x==4:
        r=float(input("Ingrese el radio del cono: "))
        g=float(input("Ingrese la generatriz del cono: "))
        h=float(input("Ingrese la altura del cono: "))

        volumen=math.pi*r**2*h/3

        print("El volumen del cono es: ", volumen)
        archivo.write('volumen=% s' %volumen + '\n')

##continuar
continua=True
while (continua):
    seleccion=cono()
    print("¿Quieres continuar (s/n)? ")
    if (input ()=="s" or input ()=="S"):
        continua=True
    else:
        continua=False
        print("Fin del programa")

archivo.close()
