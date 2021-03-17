import psycopg2
archivo=open("Promedios.txt","a")
n=int(input("Ingrese el número de personas: "))

if n>0 :
    peso_hombres=0
    peso_mujeres=0
    altura_hombres=0
    altura_mujeres=0
    cantidad_hombres=0
    cantidad_mujeres=0

    for i in range (n):
        peso= float(input("Ingrese el peso en Kg: "))
        altura= int(input("Ingrese la altura en cm: "))
        genero= input("ingrese el género de la persona (M) (F): ")

        if genero == 'M' or genero == 'm':
            peso_hombres += peso
            altura_hombres += altura
            cantidad_hombres += 1

        elif genero =='F' or genero == 'f':

            peso_mujeres += peso
            altura_mujeres += altura
            cantidad_mujeres += 1

        else:
            print("El género no existe")
    
    try:
            promedio_pesoH= peso_hombres / cantidad_hombres
    except ZeroDivisionError: #podemos obviar la especificacion del error
            promedio_pesoH=0
    try:
            promedio_alturaH= altura_hombres / cantidad_hombres
    except ZeroDivisionError: #podemos obviar la especificacion del error
            promedio_alturaH=0        

    try:
            promedio_pesoM= peso_mujeres / cantidad_mujeres
    except ZeroDivisionError: #podemos obviar la especificacion del error
            promedio_pesoM=0
    try:
            promedio_alturaM= altura_mujeres / cantidad_mujeres
    except ZeroDivisionError: #podemos obviar la especificacion del error
            promedio_alturaM=0

    conexion1 = psycopg2.connect(database="PrimerParcial", user="postgres", password="usac21")
    cursor1=conexion1.cursor()
    sql="insert into promedios(Peso, Altura, Genero) values (%s, %s, %s)"
    datos=(peso, altura, genero)
    cursor1.execute(sql,datos)
    conexion1.commit()
    conexion1.close()

    print("\nLos promedios son: "
          "\nPromedio peso de hombres: ", promedio_pesoH,
          "\nPromedio altura de hombres: ", promedio_alturaH,
          "\nPromedio peso de mujeres: ", promedio_pesoM,
          "\nPromedio altura de mujeres: ", promedio_alturaM
          )
    archivo.write("El promedio de peso de hombres es: " + 'promedio_pesoH=% s' %promedio_pesoH +'\n')
    archivo.write("El promedio de altura de hombres es " +'promedio_alturaH=% s' %promedio_alturaH +'\n')
    archivo.write("El promedio de peso de mujeres es: " + 'promedio_pesoM=% s' %promedio_pesoM +'\n')
    archivo.write("El promedio de altura de mujeres es " +'promedio_alturaM=% s' %promedio_alturaM +'\n')


else:

    print("El número ingresado no es correcto.")
archivo.close ()
