archivo=open("Bisiesto.txt", "a")
año = int(input('Introduce un año: '))
archivo.write('año=% s' %año)
if año % 4 == 0:
    if año % 100 == 0:
        if año % 400 == 0:
            print('El año es bisiesto')
            archivo.write(" El año es bisiesto"+'\n')
        else:
            print('El año no es bisiesto')
            archivo.write(" El año no es bisiesto"+'\n')
    else:
        print('El año es bisiesto.')
        archivo.write(" El año es bisiesto"+'\n')
else:
    print('El año no es bisiesto.')
    archivo.write(" El año no es bisiesto"+'\n')

archivo.close ()
