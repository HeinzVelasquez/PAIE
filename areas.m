%Areas
inicio=0;
while inicio==0;
disp('Calculo de �reas');
disp('1. Cuadrado');
disp('2. C�rculo');
disp('3. Tri�ngulo');
disp('4. Rect�ngulo');
opcion = input('Seleccione el area: ');

archivo=fopen('Areas.txt','a');
switch opcion
    case 1, disp('Cuadrado--------------------------');
        x = input('ingrese el lado: ');
        resul = x*x;
        fprintf('resultado=: %d\n',resul);
        fprintf(archivo,'El �rea es: %d\n',resul);
        back = input('Desea Continuar s/n: ','s');
            if back=='s'
                inicio=0;
                %clc
            elseif back=='n'
                inicio=1;
            end
    case 2, disp('Circulo------------------------------');
        x = input('ingrese el radio del circulo: ');
        resul = pi*x*x;
        %disp('resultado: %d\n',resul);
        fprintf('resultado=: %d\n',resul);
        fprintf(archivo,'El �rea es: %d\n',resul);
            back = input('Desea Continuar s/n: ','s');
            if back=='s'
                inicio=0;
                %clc
            elseif back=='n'
                inicio=1;
            end
    case 3, disp('Tri�ngulo---------------------');
        x = input('ingrese la base: ');
        y = input('ingrese la altura: ');
        resul = x*y/2;
        %disp('resultado: %d\n',resul);
        fprintf('resultado=: %d\n',resul);
        fprintf(archivo,'El �rea es: %d\n',resul);
            back = input('Desea Continuar s/n: ','s');
            if back=='s'
                inicio=0;
                %clc
            elseif back=='n'
                inicio=1;
            end
    case 4, disp('Rect�ngulo------------------------');
        x = input('ingrese la base: ');
        y = input('ingrese el ancho: ');
              
        resul = x*y;
        %disp('resultado: %d\n',resul);
        fprintf('resultado=: %d\n',resul);
        fprintf(archivo,'El �rea es: %d\n',resul);
            back = input('Desea Continuar s/n: ','s');
            if back=='s'
              inicio=0;
              %clc
            elseif back=='n'
              inicio=1;
            end
           
     otherwise, disp('Operaci�n No Valida');
end
end
fclose(archivo);