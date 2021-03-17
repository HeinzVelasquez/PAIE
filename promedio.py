archivo=open("Promedio.txt", "a")
x=int(input("Ingrese la primera nota: "))
y=int(input("Ingrese la segunda nota: "))
z=int(input("Ingrese la tercera nota: "))

prom=(x+y+z)/3

if (prom> 60):
    print("APROBADO ", prom)
    archivo.write('APROBADO ' + 'prom=% s' %prom + '\n')
else:
    print("REPROBADO: ",prom)
    archivo.write("REPROBADO " + 'prom=% s' %prom + '\n')

archivo.close ()
