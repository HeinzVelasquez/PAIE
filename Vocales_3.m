bandera=1;
while bandera==1;
try
a=input('Ingrese el texto:','s');
entrada=1;
catch
printf('Error ingrese una palabra \n');
entrada=0;
end_try_catch 

  if(entrada==1)
    cont1=0;
    for i=1:length(a);
      if a(i)=='a'
        cont1=cont1+1;
      endif
    end
    cont2=0;
    for i=1:length(a);
      if a(i)=='e'
        cont2=cont2+1;
      endif
    end
    cont3=0;
    for i=1:length(a);
      if a(i)=='i'
        cont3=cont3+1;
      endif
    end
    cont4=0;
    for i=1:length(a);
      if a(i)=='o'
        cont4=cont4+1;
      endif
    end
    cont5=0;
    for i=1:length(a);
      if a(i)=='u'
        cont5=cont5+1;
      endif
    end
   suma=cont1+cont2+cont3+cont4+cont5;
   printf('La palabra tiene %d',suma);
   printf(' vocales\n');
  
  endif 

back = input('Desea Continuar s/n:','s');
            if (back=='s')
                bandera=1;
            elseif(back=='n')
                bandera=0;
            endif
end