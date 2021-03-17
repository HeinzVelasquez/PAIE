bandera=1;
printf('---Suma de numeros que forman el valor ingresado---\n');

while bandera==1;
try
x = input('ingrese el numero:');
entrada=1;
catch
printf('Error ingrese un valor numerico \n');
entrada=0;
end_try_catch 

  if(entrada==1)
   conteo=0;
   for i = 1:x
     conteo=conteo+i;
   endfor
   printf('La suma de 0 hasta %d',x);
   printf(' es: %d\n',conteo);
  endif 

back = input('Desea Continuar s/n:','s');
            if (back=='s')
                bandera=1;
            elseif(back=='n')
                bandera=0;
            endif
end