'''Hay un método de cadenas llamado count que es similar a find. Lee la documentación de este método y escribe el código necesario para invocar a este método y contar el número de veces que una letra aparece en “banana”.'''

def contar(palabra:str,caracter:str) ->int:
    return palabra.count(caracter)

        
if __name__=="__main__":
    #entrada
    palabra = 'banana'
    caracter = input("Escribe la letra que quieres contar: ")

    #proceso
    conteo = contar(palabra,caracter)

    #salida
    print(conteo)