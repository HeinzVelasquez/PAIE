archivo=open("Divisores.txt", "a")
def funcion ():
    def divisores():
        n=int(input("Ingrese un número entero: "))

        resultado= [i for i in range(1, n + 1) if n % i == 0]
        archivo.write('resultado =% s' %resultado + '\n')
        return resultado
    print(divisores())


#continuar
continuar=True
while (continuar):
    seleccion=funcion()
    print("¿Quiere continuar (s/n)? ")
    if (input ()=="s" or input ()=="S"):
        continua=True
    else:
        continua=False
        print("Fin del programa")

archivo.close ()
