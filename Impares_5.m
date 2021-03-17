
archivo=fopen('Registro_5.txt','a');

for i = 1:100
     m = mod(i , 2) ;
     if (m != 0)
     fprintf(archivo,' %i',i);  
     printf(' %d',i);
     endif
 endfor
fprintf(archivo,' \n');  
fclose(archivo);


bandera=1;
while bandera==1;
try
n = input('¿Desea mostrar el historial? s/n: ','s');
entrada=1;
catch
printf('Error ingrese ina opción valida\n');
entrada=0;
end_try_catch 


if(n=='s'&&entrada==1)
  archivo=fopen('Registro_5.txt');
  arreglo=fscanf(archivo,'%i',[1,50]);
  fclose(archivo);
  printf('  %i %i \n',arreglo);
endif 

back = input('Desea Continuar s/n:','s');
            if (back=='s')
                bandera=1;
            elseif(back=='n')
                bandera=0;
            endif
end