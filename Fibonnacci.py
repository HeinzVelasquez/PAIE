archivo=open("Fibonassi.txt", "a")

rango = int(input("Cuantos numeros desea que se muestren: "))
fib=[0,1]

for i in range(rango-2):
   fib.append(fib[-1] + fib[-2])

print(fib)
archivo.write("La secuencia de Fibonacci es: " + 'fib=% s' %fib +'\n')
       
archivo.close()
