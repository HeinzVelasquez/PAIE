bandera=1;
while bandera==1;
try
a=input('Ingrese s si desea continua o n para salir:','s');
entrada=1;
catch
printf('Error ingrese un texto del menú \n');
entrada=0;
end_try_catch 

  if(a=='s')
    suma1=0;
    for i=1:100;
        suma1=suma1+i^2;
    end
    suma2=0;
    for i=1:100;
        suma2=suma2+i;
    end  
    suma2=suma2^2;
    diferencia=suma2-suma1;
    archivo=fopen('Registro_cuadrados.txt','a');
    fprintf(archivo,'La diferencia es: %i\n');
    fprintf(archivo,' %i',diferencia);  
    fprintf(archivo,' \n');  
    fclose(archivo);
    printf("La diferencia es:%d",diferencia);
    printf("\n");
  else
    printf("Error, ingrese una opción del menu\n")
  endif 
  
  
back = input('Desea Continuar s/n:','s');
            if (back=='s')
                bandera=1;
            elseif(back=='n')
                bandera=0;
            endif
end