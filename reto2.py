import os
import sys


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def printMenu(opciones):
    for i in range(len(opciones)):
        print(f'{i+1}. {opciones[i]}\n')


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


def favorito(opciones, rootOpciones):
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


def menu(opciones, opc, rootOpciones):
    if(opc >= 1 and opc <= 5):
        print(f'Usted ha elegido la opción {opc}')
        return[False, []]
    elif(opc == 6):
        selecFavorito = favorito(opciones, rootOpciones)
        return selecFavorito
    elif(opc == 7):
        print('Hasta pronto')
        return[False, []]
    else:
        print('Error')
        return [False, opciones]


def selecMenu():
    rootOpciones = ['Cambiar contraseña', 'Ingresar coordenadas actuales', 'Ubicar zona wifi más cercana', 'Guardar archivo con ubicacción cercana',
                    'Actualizar registros de zonas wifi desde archivo', 'Elegir opción de menú favorita', 'Cerrar sesión']
    reset = [True, rootOpciones]

    countErrors = 0
    while reset[0]:
        printMenu(reset[1])
        opc = int(input('Elija una opción\n'))
        reset = menu(reset[1], opc, rootOpciones=rootOpciones)

        if(reset[0] and (len(reset[1]) > 0)):
            countErrors = 0
        elif((reset[0] == False) and (len(reset[1]) > 0)):
            countErrors += 1
            reset[0] = True
        elif(len(reset[1]) == 0):
            reset[0] = False

        # print('Clear')
        clear()
        if(countErrors >= 3):
            reset[0] = False


def sesion():
    print("Bienvenido al sistema de ubicación para zonas públicas WIFI")
    default = "51659"
    defaultInv = "95615"
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


sesion()

#default = "51659"
#defaultInv = "95615"

#print('Clear outsaid')
clear()
