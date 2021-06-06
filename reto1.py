import os
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


print("Bienvenido al sistema de ubicación para zonas públicas WIFI")
default = "51659"
defaultInv = "95615"
user = input("Ingrese el usuario por favor: ")
if(user == default):
    password = input("ingrese la contraseña por favor: ")
    if(password == defaultInv):
        termino1 = 659
        termino2 = (((9+6)*5)/5)-5 + 1 -6
        captcha = int(input(f"{termino1} + {termino2}: "))
        if(captcha == (termino1 + termino2)):
            print("Sesión iniciada")
        else:
            print("Error")
    else:
        print("Error")  
else:
    print("Error")

clear()

