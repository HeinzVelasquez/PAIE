archivo=open("Factorial7.txt","a")
import psycopg2

def ingreso():
    try:
      entrada = int(input("Ingrese el numero que desea calcular:"));
     
    except:
        print("Error, ingrese valores numericos\n")
        entrada=ingreso()
    return entrada

def verificar():
    entrada=ingreso()
    cociente, residuo = divmod(entrada, 7)

    if(residuo==0 and cociente>0):
        factorial = 1
        valor=entrada
        for i in range(entrada):
            factorial=factorial*entrada
            entrada=entrada-1
            

        conexion1 = psycopg2.connect(database="Prueba", user="postgres", password="usac21")
        cursor1=conexion1.cursor()
        sql="insert into factorial7(valor, factorial) values (%s,%s)"
        datos=(valor, factorial)
        cursor1.execute(sql, datos)
        conexion1.commit()
        conexion1.close() 
        print ("El fatorial es",factorial,"****Registro Almacenado****\n")
        

    
    elif(reciduo!=0 or cociente==0):
        print("El numero ingresado no es mutiplo de 7\n")

    

verificar()
archivo.close()
