valor=input('Ingrese el primer número: ','s');
n=str2num(valor);
valor=input('Ingrese el segundo numero: ','s');
m=str2num(valor);

if n>m
  rango=n:-1:m
else
  rango=m:-1:n
endif
