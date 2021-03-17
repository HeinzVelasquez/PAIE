bandera=1;
while bandera==1;
try
x = input('ingrese primer numero:');
y = input('ingrese segundo numero:');
z = input('ingrese tercer numero:');
entrada=1;
catch
printf('Error ingrese un numero del menú \n');
entrada=0;
end_try_catch 

archivo=fopen('Registro_1.txt','a');

if(entrada==1)
    if(x>y && x>z)
      suma=x+y+z;
      fprintf(archivo,'La suma de los numeros es: %i\n',suma);
      printf('Registro guardado \n');
      printf('La suma de los numeros es: %d',suma);
    elseif(y>x && y >z)
      mult=x*y*z;
      fprintf(archivo,'La multiplicación de los numeros es: %i\n',mult);
      printf('Registro guardado \n');
      printf('La multiplicacion de los numeros es: %d\n',mult);
    elseif(z>x && z>y)
      fprintf(archivo,'Los numeros son: %i',x);
      fprintf(archivo,', %i',y);
      fprintf(archivo,', %i\n',z);
      printf('Registro guardado \n');
      printf('Los numeros son: %d',x);
      printf(', %d',y);
      printf(', %d\n',z);
    elseif(x==y && x!=z)
      fprintf(archivo,'El numero diferente es: %i\n',z);
      printf('Registro guardado \n');
      printf('El numero dstinto es: %d\n',z);
    elseif(y==z && y!=x)
      fprintf(archivo,'El numero diferente es: %i\n',x);
      printf('Registro guardado \n');
      printf('El numero dstinto es: %d\n',x);
    else
      fprintf(archivo,'Los tres numeros son iguales\n');
      printf('Registro guardado \n');
      printf('Los tres numeros son iguales \n');
    endif
  
endif 
fclose(archivo);

back = input('Desea Continuar s/n:','s');
            if (back=='s')
                bandera=1;
            elseif(back=='n')
                bandera=0;
            endif
end