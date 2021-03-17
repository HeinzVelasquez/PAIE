archivo=open("Areas.txt", "a")
import math

print("Calcular Áreas de figuras Geométricas.\n")
print("1.Cuadrado.\n2.Circulo.\n3.Triángulo.\n4.Rectángulo.\n")
x=int(input("Escoja la figura: "))
    
if x==1:
    L=int(input('Ingrese el lado: '))
    area=L*L
    print("El área del cuadrado es: ", area)
    archivo.write("Área del cuadrado es: " + 'area=% s' %area + '\n')
    
if x==2:

    R=int(input('Ingrese el radio del circulo: '))
    area=math.pi*R**2
    print("El área del círculo es: ", area)
    archivo.write("Área del circulo es: " + 'area=% s' %area +'\n')
    
if x==3:
    
    b=int(input('Ingrese la base: '))
    h=int(input('Ingrese la altura: '))
    area=b*h/2
    print("El área del triángulo es: ",area)
    archivo.write("Área del triángulo es: " + 'area=% s' %area + '\n')
  
   
if x==4:
    
    b=int(input('Ingrese la base: '))
    h=int(input('Ingrese la altura: '))
    area=b*h
    print("El área del rectángulo es: ",area)
    archivo.write("Área del rectángulo es: " + 'area=% s' %area + '\n')

archivo.close ()
    
