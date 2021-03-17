archivo=fopen('Taxi_14.txt','a');

x=input('Ingrese el año de su vehículo: ','s');
a=str2num(x);
fprintf(archivo,'Año: %d',a);
km=input('Ingrese el kilometraje: ','s');
k=str2num(km);
fprintf(archivo,' Km: %d',k);

if a<=2007 && k>=20000
  disp('Debe renovarse');
  fprintf(archivo,' Debe renovare \n');
elseif a>2007 && a<=2013 && k>=20000
  disp('Mantenimiento')
  fprintf(archivo,' Mantenimiento \n');
elseif a>2013 && k<10000
  disp('Optimas condiciones');
  fprintf(archivo,' Optimas condiciones \n');
else
  disp('Mecánico');
  fprintf(archivo,' Mecánico \n');
  
end
fclose(archivo);