bandera=1;
while bandera==1;
try
a=input('Ingrese radio del cono:');
b=input('Ingrese generatriz del cono:');
c=input('Ingrese altura del cono:');
entrada=1;
catch
printf('Error ingrese un texto del menú \n');
entrada=0;
end_try_catch 

  if(entrada=1)
    base=pi*a^2;
    arealateral=pi*a*b;
    areatotal=base+arealateral;
    volumen=b*c*a*a/3;
 
    archivo=fopen('Registro_cono.txt','a');
    fprintf(archivo,'Area de la base=: %i');
    fprintf(archivo,' %i',base); 
    fprintf(archivo,'Area lateral=: %i');
    fprintf(archivo,' %i',arealateral);   
    fprintf(archivo,'Area Total=: %i');
    fprintf(archivo,' %i',areatotal);  
    fprintf(archivo,' \n');  
    fclose(archivo);
    printf("El area de la base es:%d",base);
    printf("\n");
    printf("El area lateral es:%d",arealateral);
    printf("\n");
    printf("El area Total es:%d",areatotal);
    printf("\n");
    printf("El volumen del cono es: %d",volumen);
    printf('\n');
  else
    printf("Error, ingrese valores numericos\n");
  endif 
  
  
back = input('Desea Continuar s/n:','s');
            if (back=='s')
                bandera=1;
            elseif(back=='n')
                bandera=0;
            endif
end