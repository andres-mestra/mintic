import os
import sys


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def promedio(array):
    longitud = len(array)
    suma = sum(array)
    return suma/longitud


def printMenu(opciones):
    for i in range(len(opciones)):
        print(f'{i+1}. {opciones[i][0]}\n')


def valid(message, right, errorMsg=''):
    res = int(input(f'{message}\n'))
    if(res != right):
        print(errorMsg)
        return False

    return True


def ordenar(opciones, favorito):
    fav = opciones.pop(favorito)
    opciones.insert(0, fav)
    return opciones


def favorito(opciones):
    fav = int(input('Seleccione opción favorita\n'))
    if((fav <= 5) and (fav >= 1)):
        autorization = valid(
            'Para confirmar por favor responda: Si me giras pierdo tres unidades por eso debes colocarme siempre de pie, la respuesta es',
            5,
            'Error'
        )
        if(autorization == False):
            return [False, rootOpciones]

        autorization = valid(
            'Para confirmar por favor responda: Me separaron de mi hermano siamés, antes era un ocho y ahora soy un… la respuesta es',
            9,
            'Error'
        )
        if(autorization == False):
            return [False, rootOpciones]

        opciones = ordenar(opciones, fav-1)
        return [True, opciones]
    else:
        print('Error')
        return [False, []]


def change_password():
    global defaultInv
    password = input('Ingrese contraseña actual: ')

    if(password != defaultInv):
        print('Error')
        return False

    password = input('Ingrese contraseña nueva: ')
    if(password == defaultInv):
        print('Error')
        return False

    defaultInv = password
    return True


def input_coordenadas():
    global coordenadas

    def valid_latitud(latitud):
        if(latitud < 9.757 or latitud > 10.465):
            print('Error coordenada')
            return False
        return True

    def valid_longitud(longitud):
        if(longitud < -73.623 or longitud > -72.987):
            print('Error coordenada')
            return False
        return True

    def print_coordenadas(coordenadas):
        for i in range(len(coordenadas)):
            print(f'coordenada [latitud,longitud] {i+1} : {coordenadas[i]}')

    # rangos validos
    # latitud: xE{x >= 9.757,x  <= 10.462}
    # longitud: xE{x >= -73.623,x  <= -72.987}

    def add_coordenadas(index=None):
        if(index == None):
            for lat in range(3):
                print(f'Coordenada {lat+1}:')
                latitud = float(input('Latitud: '))
                if(valid_latitud(latitud) == False):
                    return False

                longitud = float(input('Longitud: '))
                if(valid_longitud(longitud) == False):
                    return False

                coordenadas[lat] = [latitud, longitud]
        else:
            latitud = float(input('Latitud: '))
            if(valid_latitud(latitud) == False):
                return False

            longitud = float(input('Longitud: '))
            if(valid_longitud(longitud) == False):
                return False

            coordenadas[index] = [latitud, longitud]

        return True

    if(coordenadas[0][0] == 0):
        valid = add_coordenadas()
        if(valid):
            return True
    else:
        print_coordenadas(coordenadas)
        longitudes = [coordenadas[i][-1] for i in [0, 1, 2]]
        latitudes = [coordenadas[i][0] for i in [0, 1, 2]]
        index_occidental = longitudes.index(max(longitudes))
        print(
            f'la coordenada {index_occidental+1} es la que esta más al occidente')
        print(
            f'la coordenada promedio de todos los puntos: [{round(promedio(latitudes),3)}, {round(promedio(longitudes),3)}]')
        index = int(input(
            'Presione 1,2 o 3 para actualizar la respectiva coordenadas\nPresione 0 para regresar al menu\n'))
        if(index >= 1 and index <= 3):
            add_coor = add_coordenadas(index-1)
            if(add_coor):
                return True
        elif(index == 0):
            return True
        else:
            print('Error actualización')

    return False


def menu(opciones, opc):
    if(opc >= 1 and opc <= 2):
        response = opciones[opc-1][1]()
        if(response):
            return [True, opciones]
        else:
            return [False, []]
    elif(opc >= 3 and opc <= 5):
        print(f'Usted ha elegido la opción {opc}')
        return[False, []]
    elif(opc == 6):
        selecFavorito = opciones[5][1](opciones)
        return selecFavorito
    elif(opc == 7):
        print('Hasta pronto')
        return[False, []]
    else:
        print('Error')
        return [False, opciones]


def selecMenu():
    reset = [True, rootOpciones]

    countErrors = 0
    while reset[0]:
        printMenu(reset[1])
        opc = int(input('Elija una opción\n'))
        reset = menu(reset[1], opc)

        if(reset[0] and (len(reset[1]) > 0)):
            countErrors = 0
        elif((reset[0] == False) and (len(reset[1]) > 0)):
            countErrors += 1
            reset[0] = True
        elif(len(reset[1]) == 0):
            reset[0] = False

        print('Clear selecMenu')
        # clear()
        if(countErrors >= 3):
            reset[0] = False


def sesion():
    print("Bienvenido al sistema de ubicación para zonas públicas WIFI")

    user = input("Ingrese el usuario por favor: ")
    if(user == default):
        password = input("ingrese la contraseña por favor: ")
        if(password == defaultInv):
            termino1 = 659
            termino2 = (((9+6)*5)/5)-5 + 1 - 6
            captcha = int(input(f"{termino1} + {termino2}: "))
            if(captcha == (termino1 + termino2)):
                print("Sesión iniciada")
                selecMenu()
            else:
                print("Error")
        else:
            print("Error")
    else:
        print("Error")


default = "51659"
defaultInv = "95615"
# test coord [[9.758, -73.622], [9.759, -73.621], [9.8, -73.62]]
coordenadas = [[0, 0], [0, 0], [0, 0]]
rootOpciones = [['Cambiar contraseña', change_password], ['Ingresar coordenadas actuales', input_coordenadas], ['Ubicar zona wifi más cercana'], ['Guardar archivo con ubicacción cercana'],
                ['Actualizar registros de zonas wifi desde archivo'], ['Elegir opción de menú favorita', favorito], ['Cerrar sesión']]


def main():
    sesion()
    #print("Clear main")
    clear()


if __name__ == "__main__":
    main()
