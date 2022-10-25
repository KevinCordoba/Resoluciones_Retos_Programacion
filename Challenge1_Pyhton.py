#Challenge 1
'''
 * Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso
   (Bool) según sean o no anagramas.
 * Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
 * NO hace falta comprobar que ambas palabras existan.
 * Dos palabras exactamente iguales no son anagrama.
'''
global msgNo, msgSi
msgNo =  "La palabra NO es un Anagrama"
msgSi = "La palabra es un Anagrama"

def challenge2():
    print ("Hola, este programa verifica si 2 palabras son anagramas, primero ingrese una palabra y de segundo la palabra que desea comprobar si es un anagrama. \n")
    wordA = input("Ingrese Una Palabra: ")
    print("\n")
    wordB = input("Ingrese La Palabra a Comprobar: ")
    print("\n")
    
    if (wordA == wordB):
        print(msgNo)

    else:
        if (sorted(wordA) == sorted(wordB)):
            print(msgSi)
        else:
            print(msgNo)

challenge2()
