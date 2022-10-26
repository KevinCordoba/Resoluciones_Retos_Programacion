#Sucesion de Fibonacci
'''
 * Enunciado: Escribe un programa que imprima los 50 primeros números de
   la sucesión de Fibonacci empezando en 0.
   
 * La serie Fibonacci se compone por una sucesión de números en la que el
   siguiente siempre es la suma de los dos anteriores.
   
 * 0, 1, 1, 2, 3, 5, 8, 13...
'''
def challenge3():
    i = 0
    number = 0
    last = 0
    current = 1
    
    print(i, "\n")
    i += 1
    print(i, "\n")
    i = 0
    
    while (i < 48):
        number = (current + last)
        print(number, "\n")
        last = current
        current = number
        i += 1

challenge3()
