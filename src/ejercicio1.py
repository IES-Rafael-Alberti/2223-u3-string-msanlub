'''Escribe un bucle while que comience con el último carácter en la cadena y haga un recorrido hacia atrás hasta el primer carácter en la cadena, imprimiendo cada letra en una línea independiente.'''

def invertirCadena(hola:str) ->str:
    cadena = len(hola)
    letras = []
    while cadena != 0 :
        letras.append(hola[cadena -1])
        cadena = cadena -1
    return letras
    '''while cadena < len(hola):
        letra = hola[::-1][cadena]
        cadena = cadena + 1
        #salida
        print(letra)'''

if __name__=="__main__":
    #entrada
    hola = "Hola Mundo"

    #proceso
    letras=invertirCadena(hola)

    #salida
    print(letras)
    for i in letras:
        print(i)


