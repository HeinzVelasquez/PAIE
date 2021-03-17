import psycopg2

def ingreso():
    try:
      entrada =(input("Ingrese s si desea calcular o n para salir:"));
    except:
        print("Error, ingrese una opcion del menú\n")
        entrada=ingreso()
    return entrada

def verificar():
    entrada=ingreso()
    
    if(entrada=="s"):
     
        inicio=1
        suma1=0
        for i in range(100):
            suma1=suma1+pow(i,2)
            
        suma2=0
        for i in range(100):
            suma2=suma2+i

        suma2=pow(suma2,2)
        diferencia=suma2-suma1
        print("La diferencia es: ", diferencia)
        conexion1 = psycopg2.connect(database="PrimerParcial", user="postgres", password="usac21")
        cursor1=conexion1.cursor()
        sql="insert into cuadrados(suma1, suma2, diferencia) values (%s, %s, %s)"
        datos=(suma1, suma2, diferencia)
        cursor1.execute(sql,datos)
        conexion1.commit()
        conexion1.close()

        archivo=open("Cuadrados.txt", "w")
        archivo.write("La diferencia es= %s \n"%diferencia)
        archivo.close()
        print ("****Registro Almacenado****\n")
    
    elif(entrada=="n"):
        print("Fin del programa")
        continuar=False
    else:
        print("Error, ingrese una opción del menú")
        ingreso()

continuar=True
while (continuar):
    verificar()
    print("¿Quieres continuar (s/n):")
    if (input ()== "s"):
        continuar=True
    elif(input()=="n"):
        continuar=False
        print("Fin del programa")
