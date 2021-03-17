archivo=fopen('Promedio.txt','a');

valor=input('ingrese la primera nota: ','s');
n=str2num(valor);
valor=input("ingrese la segunda nota: ", 's');
m=str2num(valor);

valor=input("ingrese la tercera nota: ",'s');
p=str2num(valor);

resultado=(n+m+p)/3;
disp(['el promedio es ' ,num2str(resultado)])
fprintf(archivo,'el promedio es: %d',resultado);
printf('Registro guardado \n');

if (resultado > 60)
  disp('Aprobado')
  fprintf(archivo,' Aprobado \n');
else
  disp('Reprobado')
  fprintf(archivo,' Reprobado \n');
endif

fclose(archivo);