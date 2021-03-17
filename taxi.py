archivo=open("Taxi.txt", "a")
import psycopg2

año=int(input("Ingrese el año de su vehículo: "))
km=int(input("Ingrese el kilometraje de su vehículo: "))
archivo.write('año=% s' %año +' ')
archivo.write('km=% s' %km + ' ')

if (año<=2007 and km>=20000):
    accion=str("Debe Renovarse")
    print(accion)
    archivo.write('Debe Renovarse' + '\n')
elif (año> 2007 and año<=2013 and km>=20000):
    accion=str("Debe realizar Mantenimiento")
    print(accion)
    archivo.write('Mantenimiento' + '\n')
elif(año>2013 and km<10000):
    accion=str("Vehículo en Optimas condiciones")
    print(accion)
    archivo.write('Optimo'+ '\n')
else:
    accion=str("mecanico")
    print(accion)
    archivo.write('Mecánico'+'\n')

    conexion1 = psycopg2.connect(database="Prueba", user="postgres", password="usac21")
    cursor1=conexion1.cursor()
    sql="insert into taxi(año, km, accion) values (%s,%s,%s)"
    datos=(año, km, accion)
    cursor1.execute(sql, datos)
    conexion1.commit()
    conexion1.close()
    print ("****Registro Almacenado****\n")
    

archivo.close ()
