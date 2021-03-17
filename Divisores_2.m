bandera=1;
while bandera==1;
try
n = input('ingrese un numero entero:');
entrada=1;
catch
printf('Error ingrese un valor numerico\n');
entrada=0;
end_try_catch 

archivo=fopen('Registro_2.txt','a');

if(entrada==1)
   z = 1;
   fprintf(archivo,'Los divisores son: %i\n');  
   printf('Los divisores son: ');
   for i = 1:n 
     m = mod(n , i) ;
     if (m == 0)
     fprintf(archivo,' %i',i);  
     printf(' %d',i);
     endif
   end
   fprintf(archivo,' \n');  
   printf('\n');
  
endif 
fclose(archivo);

back = input('Desea Continuar s/n:','s');
            if (back=='s')
                bandera=1;
            elseif(back=='n')
                bandera=0;
            endif
end