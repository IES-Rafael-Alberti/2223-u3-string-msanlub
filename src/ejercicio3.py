'''Tienes este código:

palabra = 'banana'
contador = 0


Encapsúlalo en una función llamada cuenta, y hazla genérica de tal modo que pueda aceptar una cadena y una letra como argumentos.'''

def cuenta(palabra:str,caracter:str) ->int:
    contador = 0
    for letra in palabra:
        if letra == caracter:
            contador = contador + 1
    return contador

if __name__=="__main__":
    #entrada
    palabra = input("Escribe una palabra o frase: ")
    caracter = input("Ahora escribe el caracter a contar: ")

    #proceso
    cuentas = cuenta(palabra,caracter)
    #salida
    print(cuentas)