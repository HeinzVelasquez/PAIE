archivo=open("Primo.txt","a")
x=int(2);
numero=int(input("Ingrese el número para calcular sus factores primos: "))

while (numero != 1):
    if (numero % x ==0):
        print(str(x) + " ")
        numero=numero /x
        archivo.write('x=% s' %x +'\n')

    else:
        x=x+1

archivo.close ()
