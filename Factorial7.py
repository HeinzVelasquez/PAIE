archivo = open ("Factorial.txt", "a")
#Factorial (revisar)
def factorial ():
    n= int(input("Ingrese un número positivo: "))
    if (n<0 and n != 7):
        print("El número no es válido: ")
    else:
    
        result = 1
        for i in range(n,0,-1):
            result=result*i
    
        print("El factorial de",n,"es",result)
        archivo.write('n=% s' %n)
        archivo.write('result=% s' %result + '\n')
        return result
#programa continua
continua=True
while (continua):
    seleccion=factorial()
    print("¿Quieres continuar (s/n)? ")
    if (input ()=="s" or input ()=="S"):
        continua=True
    else:
        continua=False
        print("Fin del programa")

archivo.close ()
