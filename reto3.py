import os
import sys
import math


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


def input_coordenadas():
    global coordenadas
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
        longitudes = [coordenadas[i][-1] for i in range(3)]
        latitudes = [coordenadas[i][0] for i in range(3)]
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


def zonas_wifi():
    global coordenadas
    global zonas

    def distancia(p1, p2):
        #p1 =  [latitud, longitud]
        # Radio de la Tierra en Km
        R = 6372.95477598
        delta_lat, delta_long = p2[0] - p1[0], p2[1] - p1[1]

        dist = 2 * R * math.asin(math.sqrt(
            (math.pow(math.sin(delta_lat/2), 2) +
             math.cos(p1[0])*math.cos(p2[0])*math.pow(math.sin(delta_long/2), 2))
        ))
        return dist

    def orientacion(origen, destino):
        #origen = [latitud, longitud]
        sentidos = ['', '']

        # Latitud
        if(origen[0] == destino[0]):
            sentidos[0] = 'latitud actual'
        elif(origen[0] < destino[0]):
            sentidos[0] = 'norte'
        else:
            sentidos[0] = 'sur'

        # Longitud
        if(origen[1] == destino[1]):
            sentidos[1] = 'longitud actual'
        elif(origen[1] < destino[1]):
            sentidos[1] = 'oriente'
        else:
            sentidos[1] = 'occidente'

        return sentidos

    def tiempo_promedio(distancia, medio):
        # vmedios en m/s
        vel_promedio_medios = {
            'pie': 0.483,
            'bici': 3.33 - 19.44,
            'moto': 19.44,
            'bus': 16.67 - 0.483,
            'auto': 20.83
        }
        return distancia/vel_promedio_medios[medio]

    if(coordenadas[0][0] == 0):
        print('Error sin registro de coordenadas')
        return False

    print_coordenadas(coordenadas)
    ubic = int(input(
        'Por favor elija su ubicación actual (1,2 ó 3) para calcular la distancia a los puntos de conexión\n'))
    if(ubic < 1 or ubic > 3):
        print('Error ubicación')
        return False

    ubicacion_actual = coordenadas[ubic-1]
    iterable_zonas = range(len(zonas))
    ubicacion_zonas = [zonas[i][:-1] for i in iterable_zonas]
    usuarios_zonas = [zonas[i][-1] for i in iterable_zonas]
    distancias_puntos = [
        (i, distancia(ubicacion_actual, ubicacion_zonas[i]), usuarios_zonas[i]) for i in iterable_zonas
    ]
    distancias_orden = sorted(
        distancias_puntos, key=lambda dist: dist[1]
    )
    distancias_orden = sorted(
        distancias_orden, key=lambda user: user[2]
    )
    print('Zonas wifi cercanas con menos usuarios')
    for i in range(2):
        zona = distancias_orden[i]
        coordenada = zonas[zona[0]][:-1]
        print(
            f'La zona wifi {zona[0] + 1}: ubicada en {coordenada} a {zona[1]} metros , tiene en promedio {zona[2]} usuarios'
        )
    w1 = distancias_orden[0][0] + 1
    w2 = distancias_orden[1][0] + 1
    indi = int(
        input(f'Elija {w1} o {w2} para recibir indicaciones de llegada\n')
    )
    if(indi == w1 or indi == w2):
        y, x = orientacion(ubicacion_actual, zonas[indi-1])
        print(
            f'Para llegar a la zona wifi dirigirse primero al {x} y luego hacia el {y}')
        # Distancia en la lista distancias_orden esta en kilometros, la función tiempo promedio en metros
        print(
            f'Tiempo en auto {tiempo_promedio((distancias_orden[indi][1]), "auto")}s')
        print(
            f'Tiempo en bicicleta {tiempo_promedio((distancias_orden[indi][1]), "bici")}s')
        salir = int(input('Presione 0 para salir\n'))
        if(salir == 0):
            return True
        else:
            print('Error')
            return False

    print('Error zona wifi')
    return False


def menu(opciones, opc):
    if(opc >= 1 and opc <= 3):
        response = opciones[opc-1][1]()
        if(response):
            return [True, opciones]
        else:
            return [False, []]
    elif(opc >= 4 and opc <= 5):
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
#coordenadas = [[0, 0], [0, 0], [0, 0]]
coordenadas = [[9.758, -73.622], [9.759, -73.621], [9.8, -73.62]]
zonas = [
    [10.348, -73.051, 0],
    [10.171, -73.136, 0],
    [10.259, -73.069, 67],
    [10.350, -73.043, 45]
]
rootOpciones = [
    ['Cambiar contraseña', change_password],
    ['Ingresar coordenadas actuales', input_coordenadas],
    ['Ubicar zona wifi más cercana', zonas_wifi],
    ['Guardar archivo con ubicacción cercana'],
    ['Actualizar registros de zonas wifi desde archivo'],
    ['Elegir opción de menú favorita', favorito], ['Cerrar sesión']
]


def main():
    sesion()
    print("Clear main")
    # clear()


if __name__ == "__main__":
    main()
