#Challenge 4 using Python
'''
 * Crea UNA ÚNICA FUNCIÓN (importante que sólo sea una) que sea capaz de calcular
   y retornar el área de un polígono.
   
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 
 * - Imprime el cálculo del área de un polígono de cada tipo.
 
'''
global msg1, msg2,msg3
msg1 = "La opcion ingresada no corresponde con una opcion valida. Por favor ingrese una de estas 3 opciones: Triangulo, Rectangulo o Cuadrado."
msg2 = "Para salir ingrese salir. "
msg3 = "Gracias por usar el programa. "
def challenge4():
    Run = True
    print(f'Bienvenido, En este programa podrá calcular el area de ciertos poligonos. \nLas Opciones son: Triangulo, Rectangulo y Cuadrado. \n')
    print(msg2)
    while (Run == True):
        option = input(f'\nIngrese el nombre del Poligono del cual desea conocer el area: ')
        print(f'\n')
        
        if (option.lower() == 'triangulo'):
            base = int(input(f'Ingrese el valor de la base: '))
            altura = int(input(f'Ingrese el valor de la Altura: '))
            areaT = (base * altura)/2
            print(f'El Area del Triangulo es: ', areaT, '\n')
            
        elif(option.lower() == 'rectangulo'):
            largo = int(input(f'Ingrese el valor del Largo: '))
            ancho = int(input(f'Ingrese el valor del Ancho: '))
            areaR = (largo * ancho)
            print(f'El Area del Rectangulo es: ', areaR, '\n')
            
        elif (option.lower() == 'cuadrado'):
            lado = int(input(f'Ingrese el valor del Lado: '))
            areaC = (lado * lado)
            print(f'El Area del Cuadrado es: ', areaC, '\n')
            
        elif (option.lower() == 'salir'):
            print(msg3)
            Run = False
            
        else:
            print(msg1)
        

challenge4()
        
