archivo=open("Impares.txt", "w")
impares=[i for i in range(1,101) if i%2 !=0]
print (impares)
archivo.write('impares=% s' %impares + ' ')
print ("Hay 50 números impares de 1 a 100")

archivo.close ()
