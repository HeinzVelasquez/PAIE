archivo=open("Vocales.txt", "a")
n=str(input("Ingrese una palabra: "))

contara=n.count("a")
contare=n.count("e")
contari=n.count("i")
contaro=n.count("o")
contaru=n.count("u")
contar= contara + contare + contari + contaro + contaru
print("La palabra ",n, " ", "tiene " ,contar, " vocales")
archivo.write ("La palabra " + n + ' tiene ' + 'contar=% s' %contar + " vocales")

archivo.close ()
