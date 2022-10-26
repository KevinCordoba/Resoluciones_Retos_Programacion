#Challenge 3
'''
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
'''
global msgNo, msgSi
msgNo = "El numero ingresado NO es un numero primo. \n"
msgSi = "El numero ingresado Es Un Numero Primo. \n"

def challenge3():
    n = int(input("Ingrese el numero a verificar: "))
    print(f'\n')
    if (primos(n) == True):
        print(msgSi)
        printNum()
    else:
        print(msgNo)
        printNum()

def primos(number):
    if (number < 2):
        return False

    elif (number == 2 or number == 3 or number == 5 or number == 7 or number == 11):
        #print(msgSi)
        return True
    else:
        for i in range(2,number):
            if number%i == 0:
                #print(msgNo)
                return False
        return True

#Imprime los numeros en el rango especificado con saltos de linea     
def printNum():
    print(f'Los Numeros Primos entre el 1 y 100 son los siguientes: \n')
    for i in range(1,101):
        if (primos(i)):
            print(f' EL Numero: ', i , f'\n')

#Si se quiere una lista con los primos en ese rango llamar printList() en lugar de printNum
def printList():
    Lista = []
    print(f'Los Numeros Primos entre el 1 y 100 son los siguientes: \n')
    for i in range(1,101):
        if (primos(i)):
            Lista += [i]
    print(Lista)
    
challenge3()
