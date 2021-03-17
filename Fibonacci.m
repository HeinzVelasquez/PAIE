bandera=1;
while bandera==1;
  
try
n=input('Ingrese el valor que desea calcular:');
entrada=1;
catch
printf('Error ingrese un valor numerico.  \n');
entrada=0;
end_try_catch 

 function suc=fibonacci(n)
  suc=[1 1];
  for i=1:(n-2);
    suc=[suc, suc(i)+suc(i+1)];
  end %for
 end %function
fibonacci(n)


back = input('Desea Continuar s/n:','s');
            if (back=='s')
                bandera=1;
            elseif(back=='n')
                bandera=0;
            endif
end




